import { useState } from "react";
import { uploadDataset } from "../services/datasetService";

export default function DatasetPage(){

  const [file,setFile] = useState(null);
  const [message,setMessage] = useState("");

  async function handleUpload(){

    if(!file) return;

    const res = await uploadDataset(file);

    setMessage("Dataset uploaded successfully");

  }

  return(

    <div style={{padding:"40px"}}>

      <h2>Upload Dataset</h2>

      <input
        type="file"
        onChange={(e)=>setFile(e.target.files[0])}
      />

      <br/><br/>

      <button onClick={handleUpload}>
        Upload
      </button>

      <p>{message}</p>

    </div>

  );

}