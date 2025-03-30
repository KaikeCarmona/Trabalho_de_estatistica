import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import mplcursors 

data = r".\nba_data.csv"  # Removida a vírgula

df = pd.read_csv(data, sep=',')

# Dicionario com os 3 jogadores
players = ["Shai Gilgeous-Alexander", "Nikola Jokić"]
season = [2025]

# Filtrar o DataFrame
df_filtered = df[df["player"].isin(players) & df["season"].isin(season)]

# Calcular pontos
media_de_pontos_por_temporada = df_filtered.groupby("player")["pts_per_game"].mean()
print(f"Media de pontos nessa temporada: {media_de_pontos_por_temporada}\n")

print("\n------------------------\n")
media_de_rebotes_por_temporada = df_filtered.groupby("player")["trb_per_game"].mean()
print(f"Media de rebotes nessa temporada: {media_de_rebotes_por_temporada}\n")

print("\n------------------------\n")
# Calcular assists
media_de_asists_por_temporada = df_filtered.groupby("player")["ast_per_game"].mean()
print(f"Media de assistencias nessa temporada: {media_de_asists_por_temporada}")

print("\n------------------------\n")

# Exibir os jogadores e o número de arremessos de 3 pontos por jogo
modo_arremessos_3p = df_filtered['x3p_per_game'].mode()[0]
print(f"Na temproara, os jogadores tiveram uma moda de {modo_arremessos_3p} arremessos de 3 tentados:")

print("\n------------------------\n")


# Quartis: a media dos pontos por jogo em uma temporada 
quartis_dict = {}
for player in players:
    quartis = df[df['player'] == player]['pts_per_game'].quantile([0.25, 0.50, 0.75])
    quartis_dict[player] = quartis
    print(f"Quartis de pontos por jogo de {player}:\nQ1 (25%): {quartis[0.25]}\nQ2 (Mediana/50%): {quartis[0.50]}\nQ3 (75%): {quartis[0.75]}")


print("\n------------------------\n")


# Amplitude: a diferença entre o maior e o menor número de assistencias por jogo em uma temporada
amplitude_dict = {}
for player in players:
    amplitude = df[df['player'] == player]['pts_per_game'].max() - df[df['player'] == player]['pts_per_game'].min()
    amplitude_dict[player] = amplitude
    print(f"Amplitude de pontos por jogo de {player}: {amplitude}")

print("\n------------------------\n")

# Amplitude Interquartil: a diferença entre o terceiro e o primeiro quartil de pontos por jogo em uma temporada
aiq_dict = {}
for player in players:
    q1 = df[df['player'] == player]['pts_per_game'].quantile(0.25)
    q3 = df[df['player'] == player]['pts_per_game'].quantile(0.75)
    aiq = q3 - q1
    aiq_dict[player] = aiq
    print(f"Amplitude Interquartil de pontos por jogo de {player}: {aiq}")

print("\n------------------------\n")

# Desvio Absoluto Médio
mad_dict = {}
for player in players:
    pontos = df[df["player"] == player]["pts_per_game"] 
    media_pontos = np.mean(pontos)
    # Calcula o Desvio Absoluto Médio
    mad = np.mean(np.abs(pontos - media_pontos))
    print(f"Desvio Absoluto Médio de pontos por jogo de {player}: {mad:.2f}")
    mad_dict[player] = mad
    

print("\n------------------------\n")

# Variância
variancia_dict = {}
for player in players:
    rebotes = df[df["player"] == player]["ast_per_game"] 
    variancia_de_rebotes = rebotes.var()
    print(f"Variância de assistências por jogo de {player}: {variancia_de_rebotes:.2f}")
    variancia_dict[player] = variancia_de_rebotes

print("\n------------------------\n")



# Desvio Padrao: desvio padrão de pontos por jogo em uma temporada
for player in players:
    pontos = df[df['player'] == player]['pts_per_game']
    desvio_padrao_pontos = np.std(pontos)
    print(f"Desvio padrão de pontos por jogo de {player}: {desvio_padrao_pontos:.2f}")

print("\n------------------------\n")
def gerar_analise_txt():
    # Gerando o relatório em um arquivo .txt
    relatorio = ""

    # Adicionar resultados sobre Média de Pontos por Temporada
    relatorio += "Média de Pontos por Temporada:\n"
    relatorio += f"{media_de_pontos_por_temporada}\n\n"

    # Adicionar resultados sobre Média de Rebotes por Temporada
    relatorio += "Média de Rebotes por Temporada:\n"
    relatorio += f"{media_de_pontos_por_temporada}\n\n"

    # Adicionar resultados sobre Média de Assistências por Temporada
    relatorio += "Média de Assistências por Temporada:\n"
    relatorio += f"{media_de_asists_por_temporada}\n\n"

    # Adicionar resultados sobre Moda de Arremessos de 3 pontos
    relatorio += f"Moda de Arremessos de 3 Pontos na Temporada: {modo_arremessos_3p}\n\n"

    # Adicionar resultados sobre Quartis
    relatorio += "Quartis de Pontos por Jogo:\n"
    for player in players:
        quartis = quartis_dict[player]
        relatorio += f"Jogador: {player}\n"
        relatorio += f"Q1 (25%): {quartis[0.25]}\n"
        relatorio += f"Q2 (Mediana/50%): {quartis[0.50]}\n"
        relatorio += f"Q3 (75%): {quartis[0.75]}\n\n"

    # Adicionar resultados sobre Amplitude
    relatorio += "Amplitude de Pontos por Jogo:\n"
    for player in players:
        relatorio += f"{player}: {amplitude_dict[player]}\n"
    relatorio += "\n"

    # Adicionar resultados sobre Amplitude Interquartil (IQR)
    relatorio += "Amplitude Interquartil de Pontos por Jogo:\n"
    for player in players:
        relatorio += f"{player}: {aiq_dict[player]}\n"
    relatorio += "\n"

    # Adicionar resultados sobre Desvio Absoluto Médio
    relatorio += "Desvio Absoluto Médio de Pontos por Jogo:\n"
    for player in players:
        relatorio += f"{player}: {mad_dict[player]:.2f}\n"
    relatorio += "\n"

    # Adicionar resultados sobre Variância
    relatorio += "Variância de Assistências por Jogo:\n"
    for player in players:
        relatorio += f"{player}: {variancia_dict[player]:.2f}\n"
    relatorio += "\n"

    # Adicionar resultados sobre Desvio Padrão
    relatorio += "Desvio Padrão de Pontos por Jogo:\n"
    for player in players:
        relatorio += f"{player}: {np.std(df[df['player'] == player]['pts_per_game']):.2f}\n"
    relatorio += "\n"

    # Salvando o relatório em um arquivo .txt com o encoding correto
    with open("relatorio_nba.txt", "w", encoding="utf-8") as file:
        file.write(relatorio)

    print("Relatório gerado com sucesso!")
gerar_analise_txt()


fig, axes = plt.subplots(3, figsize=(10, 10))


# 1. Gráfico de Barras: Média de Pontos por Temporada
sns.barplot(x=media_de_pontos_por_temporada.values, y=media_de_pontos_por_temporada.index, ax=axes[0], palette="coolwarm", orient='h')
axes[0].set_title("Média de Pontos por Temporada")
axes[0].set_xlabel("Média de Pontos")
axes[0].set_ylabel("Jogadores")

# 3. Gráfico de Barras: Média de Assistências por Temporada
sns.barplot(x=media_de_asists_por_temporada.values, y=media_de_asists_por_temporada.index, ax=axes[1], palette="coolwarm", orient='h')
axes[1].set_title("Média de Assistências por Temporada")
axes[1].set_xlabel("Média de Assistências")
axes[1].set_ylabel("Jogadores")

# 4. Gráfico de Barras: Média de Rebotes por Temporada
sns.barplot(x=media_de_rebotes_por_temporada.values, y=media_de_rebotes_por_temporada.index, ax=axes[2], palette="coolwarm", orient='h')
axes[2].set_title("Média de Rebotes por Temporada")
axes[2].set_xlabel("Média de Assistências")
axes[2].set_ylabel("Jogadores")





# Habilitando o cursor interativo nos gráficos
mplcursors.cursor(axes[0], hover=True)  # Para o gráfico de barras de média de pontos
mplcursors.cursor(axes[1], hover=True)  # Para o gráfico de barras de média de assistências
mplcursors.cursor(axes[2], hover=True)  # Para o gráfico de dispersão de pontos

# Ajusta o layout para evitar sobreposição de elementos
plt.tight_layout()

# Exibir os gráficos
plt.show()
