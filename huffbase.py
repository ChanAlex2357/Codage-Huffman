# Exemple d'utilisation
texte_exemple = "le chat mange le poisson et le chat dort"
m, s, p = huffman_base(texte_exemple)

print(f"Nombre total de mots (m): {m}")
print("\nListe des mots uniques (s):")
for mot in s:
    print(f"- {mot}")

print("\nProbabilités (p):")
for mot, prob in p.items():
    print(f"{mot}: {prob:.3f}")