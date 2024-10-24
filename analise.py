import pandas as pd
import seaborn as sns
import sys

def extrair_dados():
    df = pd.DataFrame({
        'Ano': [2020, 2021, 2022],
        'Vendas': [100, 150, 200]
    })
    df.to_csv('dados.csv', index=False)
    return df

def plotar_grafico(df, titulo):
    sns.set(style="whitegrid")
    grafico = sns.lineplot(x='Ano', y='Vendas', data=df, marker='o', label='Vendas')
    grafico.set(title=titulo, xlabel='Ano', ylabel='Vendas')
    grafico.get_figure().savefig(f'{titulo}.png')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Uso: python analise.py <nome-do-grafico>")
    
    df = extrair_dados()
    plotar_grafico(df, sys.argv[1])