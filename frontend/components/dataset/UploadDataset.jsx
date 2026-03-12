export default function UploadDataset(){

  async function upload(file){

    const form = new FormData();
    form.append("file", file);

    await fetch("http://localhost:8000/upload",{
      method:"POST",
      body:form
    });

    alert("Dataset uploaded");
  }

  return(

    <div>

      <input
        type="file"
        onChange={(e)=>upload(e.target.files[0])}
      />

    </div>

  );
}