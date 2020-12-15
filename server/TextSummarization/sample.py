import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
import time

import torch as T
import torch.nn as nn
import torch.nn.functional as F
from TextSummarization.model import Model

from TextSummarization.data_util import config, data
from TextSummarization.data_util.batcher import Batcher
from TextSummarization.data_util.data import Vocab
from TextSummarization.train_util import *
from TextSummarization.beam_search import *
from rouge import Rouge
import argparse

def get_cuda(tensor):
    if T.cuda.is_available():
        tensor = tensor.cuda()
    return tensor

class Evaluate(object):
    def __init__(self, data_path, opt, batch_size = config.batch_size):
        self.vocab = Vocab(config.vocab_path, config.vocab_size)
        self.batcher = Batcher(data_path, self.vocab, mode='eval',
                               batch_size=batch_size, single_pass=True)
        self.opt = opt
        time.sleep(5)

    def setup_valid(self):
        self.model = Model()
        self.model = get_cuda(self.model)
        checkpoint = T.load(os.path.join(config.save_model_path, self.opt.load_model))
        self.model.load_state_dict(checkpoint["model_dict"])

    # self.print_original_predicted(decoded_sents, ref_sents, article_sents, load_file)
    def print_original_predicted(self, decoded_sents, ref_sents, article_sents, loadfile):
        # filename = "test_"+loadfile.split(".")[0]+".txt"
        filename = "E:\\CSC4160\\data\\test_output.txt"
        print(f"file name {filename}")
        # with open(os.path.join("data",filename), "w") as f:
        with open(filename, "w+", encoding="utf-8") as f:
            for i in range(len(decoded_sents)):
                f.write("article: "+article_sents[i] + "\n")
                f.write("ref: " + ref_sents[i] + "\n")
                f.write("dec: " + decoded_sents[i] + "\n\n")

    def evaluate_batch(self, print_sents = True):

        self.setup_valid()
        batch = self.batcher.next_batch()
        start_id = self.vocab.word2id(data.START_DECODING)
        end_id = self.vocab.word2id(data.STOP_DECODING)
        unk_id = self.vocab.word2id(data.UNKNOWN_TOKEN)
        decoded_sents = []
        ref_sents = []
        article_sents = []
        rouge = Rouge()

        # start_time = time.time()
        # test_batch = 0
        while batch is not None:
            enc_batch, enc_lens, enc_padding_mask, enc_batch_extend_vocab, extra_zeros, ct_e = get_enc_data(batch)

            with T.autograd.no_grad():
                enc_batch = self.model.embeds(enc_batch)
                enc_out, enc_hidden = self.model.encoder(enc_batch, enc_lens)

            #-----------------------Summarization----------------------------------------------------
            with T.autograd.no_grad():
                pred_ids = beam_search(enc_hidden, enc_out, enc_padding_mask, ct_e, extra_zeros, enc_batch_extend_vocab, self.model, start_id, end_id, unk_id)

            for i in range(len(pred_ids)):
                decoded_words = data.outputids2words(pred_ids[i], self.vocab, batch.art_oovs[i])
                if len(decoded_words) < 2:
                    decoded_words = "xxx"
                else:
                    decoded_words = " ".join(decoded_words)
                decoded_sents.append(decoded_words)
                abstract = batch.original_abstracts[i]
                article = batch.original_articles[i]
                ref_sents.append(abstract)
                article_sents.append(article)

            # test_batch_time = time.time() - start_time
            # start_time = time.time()
            # print("Current test batch", test_batch)
            # print("Testing time", test_batch_time)
            # test_batch += 1

            batch = self.batcher.next_batch()

        load_file = self.opt.load_model

        if print_sents:
            self.print_original_predicted(decoded_sents, ref_sents, article_sents, load_file)
            return decoded_sents

        # scores = rouge.get_scores(decoded_sents, ref_sents, avg = True)
        # if self.opt.task == "test":
        #     print(load_file, "scores:", scores)
        # else:
        #     rouge_l = scores["rouge-l"]["f"]
        #     print(load_file, "rouge_l:", "%.4f" % rouge_l)

def main(myconfig):
    opt = myconfig

    eval_processor = Evaluate(config.use_data_path, opt)
    result = eval_processor.evaluate_batch()
    return result

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--task", type=str, default="test", choices=["validate","test"])
    # parser.add_argument("--start_from", type=str, default="0001000.tar")
    # parser.add_argument("--load_model", type=str, default="E:/4160/TextSummarization/data/saved_models/0050000.tar")
    # opt = parser.parse_args()

    # eval_processor = Evaluate(config.use_data_path, opt)
    # eval_processor.evaluate_batch()
    main()
