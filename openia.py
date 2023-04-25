import openai
import tkinter as tk

# Ingresa tu API key de OpenAI aquí
openai.api_key = "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"

# Función que realiza la solicitud a la API de OpenAI y devuelve la respuesta
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text.strip()

# Función que se llama cuando se hace clic en el botón de enviar
def send_message():
    # Obtiene el mensaje del cuadro de entrada
    message = user_input.get()

    # Añade el mensaje a la ventana de chat
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "Usuario: " + message + "\n")
    chat_log.config(state=tk.DISABLED)

    # Genera una respuesta utilizando la API de OpenAI
    response = generate_response(message)

    # Añade la respuesta a la ventana de chat
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "Chatbot: " + response + "\n")
    chat_log.config(state=tk.DISABLED)

    # Borra el cuadro de entrada
    user_input.delete(0, tk.END)

# Crea la ventana de la aplicación
root = tk.Tk()
root.title("Chatbot")

# Crea la ventana de chat
chat_log = tk.Text(root, state=tk.DISABLED)
chat_log.pack()

# Crea el cuadro de entrada y el botón de enviar
user_input = tk.Entry(root)
user_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.pack(side=tk.RIGHT)

# Ejecuta la aplicación
root.mainloop()
