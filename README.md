# Code README

This repository contains code for a web application that generates creative tales based on user input prompts. It utilizes the AI21 language model and the Streamlit framework for the user interface.

## Setup

1. Clone the repository to your local machine.
2. Create a file named `apikey.py` in the same directory as the code.
3. Obtain an API key from AI21 and assign it to the variable `apikey` inside `apikey.py`.

```python
apikey = "YOUR_API_KEY"
```
4. Save the apikey.py file.

## Running the Code

To run the code, follow these steps:

1. Make sure you have Python installed on your machine.
2. Install the required dependencies by running the following command:

```bash
pip install langchain streamlit
```
3. Run the application using the following command:
```bash
streamlit run testapp.py
```
- You may alternatively visit http://localhost:8501 to access the application.

## Usage

1. Enter the number of prompts you want processed by the Large Language Model (LLM) in the provided text input field.
2. For each prompt, enter your desired prompt text in the corresponding text input field. Press Enter or click outside the input field to submit the prompt.
3. The entered prompts will be displayed below the input fields.
4. Script templates will be created based on the entered prompts. These templates use the entered prompts and include a placeholder variable `{title}` for further customization.
5. The created script templates will be displayed below the entered prompts.
6. The templates will be linked together to form chains. Each chain consists of two LLMChain instances that are connected in sequence.
7. The chains will be displayed below the script templates.
8. Enter your final prompt in the text input field labeled "Enter your prompt". Press Enter or click outside the input field to submit the prompt.
9. The chain with the first template as the prompt will be executed based on the final prompt entered.
10. The response generated by the chain will be displayed.

# Example
### Chain Length
- Enter how many prompts you want processed by the Large Language Model
- Input: **3**
### Prompt 1
- "Generate an epic tale relating to name "
### Prompt 2
- Prompt: "Add Woof woof to the start of this title "

### User Input
- Enter your final prompt: **Arnav**

### LLM Processing
#### Prompt 1
- Input: "Arnav"
- Prompt: "Generate an epic tale relating to name Arnav"
- Output: "The tall, rising tale of legend, Arnav the great"

#### Prompt 2
- Input: "The tall, rising tale of legend, Arnav the great"
- Prompt: "Add Woof woof to the start of this title The tall, rising tale of legend, Arnav the great"
- Output: "Woof woof The tall, rising tale of legend, Arnav the great"

**Note:** If the user interface appears differently or encounters any issues, make sure to have the necessary dependencies installed and properly configured.

Feel free to customize the prompts, template structure, or other aspects of the code to suit your specific requirements.

For any questions or support, please contact arnavpd@gmail.com.
