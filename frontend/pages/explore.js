import { useEffect, useState } from "react";
import { listDatasets } from "../services/datasetService";

export default function Explore(){

  const [datasets,setDatasets] = useState([]);

  useEffect(()=>{

    async function load(){

      const data = await listDatasets();

      setDatasets(data);

    }

    load();

  },[]);

  return(

    <div style={{padding:"40px"}}>

      <h2>Available Datasets</h2>

      {datasets.map((d)=>(
        <div key={d.id} style={{marginBottom:"10px"}}>
          {d.name}
        </div>
      ))}

    </div>

  );

}