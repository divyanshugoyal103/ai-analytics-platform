import { post } from "./api";

export async function runQuery(question, dataset) {

  return post("/query", {
    question,
    dataset
  });

}