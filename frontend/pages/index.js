import Link from "next/link";

export default function Home() {

  return (

    <div style={{padding:"40px"}}>

      <h1>AI Analytics Platform</h1>

      <p>
        Upload datasets and ask questions in natural language.
      </p>

      <div style={{marginTop:"20px"}}>

        <Link href="/dataset">
          <button>Upload Dataset</button>
        </Link>

        <Link href="/dashboard">
          <button style={{marginLeft:"10px"}}>
            Open Dashboard
          </button>
        </Link>

        <Link href="/explore">
          <button style={{marginLeft:"10px"}}>
            Explore Data
          </button>
        </Link>

      </div>

    </div>

  );

}