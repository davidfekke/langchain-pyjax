import os
import requests
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain.schema.runnable import RunnableSequence
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
from langchain_openai import OpenAI

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

llm = OpenAI(temperature=0.9)


def generate_prompt() -> PromptTemplate:
  """
  Generate a detailed prompt for DALL·E using LangChain's PromptTemplate.
  """

  prompt = PromptTemplate(
      input_variables=["image_desc"],
      template="Generate a detailed prompt to generate an image based on the following description: {image_desc}",
  )

  return prompt

def generate_image(prompt: PromptTemplate, image_description: str) -> str:
  """
  Call OpenAI's image API to generate an image based on the prompt.
  Returns the URL of the generated image.
  """
  
  prompt_text = prompt.format(image_desc=image_description)

  image_url = DallEAPIWrapper().run(prompt_text)
  return image_url

def download_image(image_url: str, file_path: str):
  """
  Download the image from the given URL and save it to a local file.
  """
  r = requests.get(image_url)
  if r.status_code == 200:
    with open(file_path, "wb") as f:
      f.write(r.content)
    print(f"Image successfully saved to {file_path}")
  else:
    print("Failed to download image.")

if __name__ == "__main__":
  # Example description to generate a prompt for DALL·E.
  description = "a futuristic cityscape at sunset with flying cars and neon lights"
  
  # Create a creative prompt for DALL·E using LangChain.
  prompt = generate_prompt()
  print(f"Generated Prompt:\n{prompt}\n")
  
  # Generate image using OpenAI's API.
  image_url = generate_image(prompt, description)
  print(f"Image URL: {image_url}\n")
  
  # Download and save the PNG image locally.
  output_file = "generated_image.png"
  download_image(image_url, output_file)
