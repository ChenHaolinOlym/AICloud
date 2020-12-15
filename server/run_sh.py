from ImagetoText.sample import main as itt_main
from TextSummarization.prepare import main as pre_main
from TextSummarization.sample import main as sam_main
import ImagetoText.config as itt_config
import TextSummarization.config as ts_config
import config

def itt(filepath):
    itt_config.image=filepath
    return itt_main(itt_config)

def ts(text):
    with open('E:\\4160\\TextSummarization\\data\\unfinished_used\\article.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    pre_main()
    result = sam_main(config)
    print(result)
    return result[0]

    