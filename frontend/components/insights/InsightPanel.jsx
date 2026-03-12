export default function InsightPanel({text}){

  return(

    <div style={{
      background:"#111",
      padding:"20px",
      marginTop:"20px",
      borderRadius:"10px"
    }}>

      <h3>Insights</h3>

      <p>{text}</p>

    </div>

  );

}