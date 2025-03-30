from string import Template

def generate_latex_table(data,cpu_model,gpu_model, cpu_count,cpu_physical_count, memory):
    with open('data/template.tex', 'r',encoding='utf-8') as template_file:
        latex_template = template_file.read()
    table_template = Template(latex_template)
    execution_times = [data[1] for data in data]
    cores = [data[0] for data in data]
    table_content = ""
    plot_content = ""
    for i in range(len(cores)):
        table_content += f"{cores[i]} & {execution_times[i]} \\\\\n"
        plot_content += f"({cores[i]}, {execution_times[i]})\n"

    latex_content = table_template.substitute(TABLE=table_content, PLOT=plot_content, 
    MODEL=cpu_model, GPU_MODEL=gpu_model, CPU=cpu_count,CPU_PHYSICAL=cpu_physical_count, MEMORY=memory)
    with open('data/tabela.tex', 'w', encoding='utf-8') as output_file:
        output_file.write(latex_content,)
    print("Arquivo LaTeX gerado com sucesso em 'data/tabela.tex'.")



def main():
    data = [
        (1, 0.5),
        (2, 0.3),
        (4, 0.2),
        (6, 0.15),
        (8, 0.1),
        (10, 0.08),
        (12, 0.07),
        (14, 0.06),
        (16, 0.05),
        (18, 0.04)
    ]
    generate_latex_table(data, cpu_count=24, memory="16 GB")
if __name__ == '__main__':
    main()
