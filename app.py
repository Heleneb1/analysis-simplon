import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')
figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')


# Analyse des Ventes
données["ca"] = données["prix"] * données["qte"]

ca_produit = données.groupby("produit")["ca"].sum().reset_index()

fig_ca_produit = px.bar(
    ca_produit,
    color="produit",
    x='produit',
    y='ca',
    color_discrete_sequence=['green','orange','red'],
    title='Chiffre d\'affaires par produit'
)

ca_total = données["ca"].sum()


fig_ca_total = go.Figure(go.Indicator(
    mode="number",
    value=ca_total,
    title='Chiffre d\'affaires total'
))

ca_region=données.groupby("region")["ca"].sum().reset_index()
fig_ca_region = px.bar(ca_region,
                       x="region",
                       y='ca',
                       color="region",
                       color_discrete_sequence=['red','blue'],
                       title="Chiffre d'affaires par région"
                       )

produit_vente= données.groupby("produit")['qte'].sum().sort_values(ascending=False).reset_index()

fig_produit_vente = px.bar(produit_vente,
                         x='produit',
                         y='qte',
                         color="produit",
                         color_discrete_sequence=['green','orange','red'],
                        title='Quantité vendue par produit'
                        )

produit_region = données.groupby(["region", "produit"])["ca"].sum().reset_index()
fig_ca_produit_region = px.bar(
    produit_region,
    x='produit',   
    y='ca',
    barmode='group',
    color='region', 
    title="CA produit par région"
)


figure.write_html('ventes-par-region.html')
print('ventes-par-région.html généré avec succès !')

fig_ca_total.write_html('chiffre-affaire-total.html')
fig_ca_region.write_html('chiffre-affaire-region.html')
fig_produit_vente.write_html("quantité-vente-produit.html")
fig_ca_produit.write_html("ca-produit.html")
fig_ca_produit_region.write_html("ca-produit-region.html")


