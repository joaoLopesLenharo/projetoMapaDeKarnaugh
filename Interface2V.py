import tkinter as tk
from map import karnaugh_map

def criar_interface():
    global ui_root, ui_labels, ui_buttons, ui_sol_text

    ui_root = tk.Tk()
    ui_root.minsize(270, 270)
    ui_root.title("Minimizador de Mapa de Karnaugh")
    ui_root.tk_setPalette("azure")

    ui_frame = tk.Frame(ui_root)
    ui_frame.grid(row=0, column=1, padx=5, pady=5)

    ui_set_frame = tk.Frame(ui_root)
    ui_set_frame.grid(row=0, column=0, padx=5, pady=5)
    ui_selection_frame = tk.Frame(ui_root)
    ui_selection_frame.grid(row=0, column=2, padx=5, pady=5)
    ui_sol_frame = tk.Frame(ui_root)
    ui_sol_frame.grid(row=1, columnspan=3, padx=5, pady=5)

    ui_result_label = tk.Label(ui_sol_frame, text="Resultado:")
    ui_result_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    ui_sol_text = tk.Entry(ui_sol_frame, bg="floral white", fg="black", width=60)
    ui_sol_text.grid(row=0, column=1, padx=5, pady=5)

    ui_solve_button = tk.Button(ui_selection_frame, bg="lavender", text="Resolver", fg="black", command=resolver)
    ui_solve_button.grid(row=0, column=0, padx=5, pady=5)

    ui_button_color = "white"
    ui_buttons = {}
    ui_labels = {}

    for i in range(1, 3):
        for j in range(1, 3):
            ui_labels[f"label_{i}_{j}"] = criar_string_var()
            ui_labels[f"label_{i}_{j}"].set("0")

            label = tk.Label(ui_frame, textvariable=ui_labels[f"label_{i}_{j}"], width=2, height=2, background="white smoke")
            label.grid(column=j-1, row=i-1)

            ui_buttons[f"button_{i}_{j}"] = tk.Button(ui_set_frame, bg=ui_button_color, text=f"Atribuir {i-1},{j-1}", command=lambda i=i, j=j: botao_pressionado(i, j))
            ui_buttons[f"button_{i}_{j}"].grid(row=i, column=j, padx=2, pady=2)

def criar_string_var():
    return tk.StringVar()

def botao_pressionado(linha, coluna):
    global ui_labels

    label_var = ui_labels[f"label_{linha}_{coluna}"]
    label_var.set("1" if label_var.get() == "0" else "0")

def obter_mapa():
    global ui_labels

    ui_sol_text.delete(0, tk.END)
    ui_sol_text.insert(0, obter_tabela_verdade())

def obter_tabela_verdade():
    valores_mapa = []
    for i in range(1, 3):
        for j in range(1, 3):
            valores_mapa.append(int(ui_labels[f"label_{i}_{j}"].get()))
    return str(valores_mapa)

def resolver():
    tabela_verdade = obter_tabela_verdade()
    expressao_minimizada = karnaugh_map(tabela_verdade)
    print(tabela_verdade)
    ui_sol_text.delete(0, tk.END)
    ui_sol_text.insert(0, expressao_minimizada)

criar_interface()
ui_root.mainloop()
