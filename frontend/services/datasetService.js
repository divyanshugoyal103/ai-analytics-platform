const API = "http://localhost:8000";

export async function uploadDataset(file) {

  const form = new FormData();
  form.append("file", file);

  const res = await fetch(`${API}/upload`, {
    method: "POST",
    body: form
  });

  return res.json();
}

export async function listDatasets() {

  const res = await fetch(`${API}/datasets`);

  return res.json();

}

export async function getDataset(datasetId){

  const res = await fetch(`${API}/datasets/${datasetId}`);

  return res.json();

}