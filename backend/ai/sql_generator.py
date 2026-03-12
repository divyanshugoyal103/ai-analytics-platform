import json
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Preload metadata for schema awareness (mock for the demo)
def load_schema_metadata(dataset):
    metadata_path = f"./datasets/{dataset}_metadata.json"
    with open(metadata_path, "r") as file:
        return json.load(file)

def generate_sql(question: str, dataset: str) -> str:
    """
    Generates an SQL query from a natural language question
    using schema metadata and LangChain.
    """
    # Load dataset metadata
    metadata = load_schema_metadata(dataset)
    schema_description = "\n".join(
        [f"{col} ({dtype})" for col, dtype in metadata["column_types"].items()]
    )

    # Prompt template for SQL generation
    prompt_template = PromptTemplate(
        input_variables=["question", "schema"],
        template=(
            "You are an SQL expert. Based on the following schema:\n"
            "{schema}\n"
            "Write an SQL query to accomplish this request: {question}"
        ),
    )

    # LLM initialization with LangChain
    llm = OpenAI(model="text-davinci-003")
    prompt = prompt_template.format(question=question, schema=schema_description)

    # Generate SQL
    generated_query = llm(prompt)

    return generated_query.strip()