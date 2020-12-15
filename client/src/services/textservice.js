import http from "./http-common";

class TextService {
  upload(text, onUploadProgress) {
    let formData = new FormData();

    formData.append("text", text);

    return http.post("/ts", formData, {
      headers: {
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "multipart/form-data"
      },
      onUploadProgress
    });
  }

  getFiles() {
    return http.get("/files");
  }
}

export default new TextService();