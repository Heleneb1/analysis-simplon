SELECT * FROM ventes;
-- CA total
SELECT SUM(c3 * c4)AS Chiffre_affaires_total 
FROM ventes;
-- Chiffre d'affaires par région
SELECT c5 As région, SUM(c3 * c4)AS Chiffre_affaires_region 
from ventes
GROUP BY c5
ORDER BY Chiffre_affaires_region DESC;
-- Chiffre d'affaires par produit
SELECT c2 AS produit, SUM(c3 * c4)AS Chiffre_affaires_produit 
from ventes
GROUP BY c2
ORDER BY Chiffre_affaires_produit DESC;
-- vente par produit
SELECT c2 As produit, SUM(c4) AS total_vente_produit
FROM ventes
Group By c2
ORDER by  total_vente_produit DESc;
