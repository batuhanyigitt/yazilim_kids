import spacy

nlp = spacy.load("en_core_web_sm")

text = "Albert Einstein was a German-born theoretical physicist who developed the theory of relativity."

doc = nlp(text)

print("Tokenization:")
for token in doc:
    print(token.text)

print("\nMorphological Analysis:")
for token in doc:
    print(f"Token: {token.text}, Lemma: {token.lemma_}, POS: {token.pos_}, Tag: {token.tag_}")

print("\nNamed Entity Analysis:")
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")

print("\nDependency Parsing:")
for token in doc:
    print(f"Token: {token.text}, Dependency: {token.dep_}, Head Token: {token.head.text}")

