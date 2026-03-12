import QueryBox from "../components/query/QueryBox";
import UploadDataset from "../components/dataset/UploadDataset";

export default function Dashboard(){

  return(

    <div style={{padding:"40px"}}>

      <h1>AI Analytics Dashboard</h1>

      <UploadDataset />

      <QueryBox />

    </div>

  )

}