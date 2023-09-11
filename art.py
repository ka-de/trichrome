import random
import pyperclip

artists = {
    "Dmitriy Bessonov": 2,
    "Ruan Jia": 1,
    "Marguerite Sauvage": 1,
    "Patrick Gleason": 1,
    "Mario Alberti": 1,
    "Sergey Kolesov": 1,
    "Zhaozhe Deng": 1,
    "Kael Ngu": 1,
    "Hicham Habchi": 1,
    "Weilun Ng": 1,
    "Muyang Xu": 1,
    "Christian Bravery": 1,
    "Bastien Grivet": 1,
    "Artur Sadlos": 1,
    "Liu Xiao": 1,
    "Andreas Rocha": 1,
    "Ivan Rastrigin": 1,
    "Xi Zhang": 1,
    "Halil Ural": 1,
    "Edouard Caplain": 1,
    "Aaron Beck": 1,
    "Brad Wright": 1,
    "Andrew March": 1,
    "Aleksi Briclot": 1,
    "Donglu Yu": 1,
    "Adrian Smith": 1,
    "Victor Hugo Harmatiuk": 1,
    "Jason Horley": 1,
    "Pascal Blanché": 1,
    "Matt Rhodes": 1,
    "Ivan Khotenov": 1,
    "Neil Ross": 1,
    "Eric Cousin": 1,
    "Robin Har": 1,
    "WenXu Xu": 1,
    "Craig Mullins": 1,
    "Jeremy Love": 1,
    "Houston Sharp": 1,
    "Martin Deschambault": 1,
    "Sergei Sarichev": 1,
    "Maria Panfilova": 1,
    "Wangjie Li": 1,
    "Alex Figini": 1,
}

# Define dead artists with weights
dead_artists = {
    "Leonardo da Vinci": 1,
    "Michelangelo Buonarroti": 1,
    "Raphael": 1,
    "Caravaggio": 1,
    "Rembrandt van Rijn": 1,
    "Vermeer": 1,
    "Titian": 1,
    "Hieronymus Bosch": 1,
    "Pieter Bruegel the Elder": 1,
    "Sandro Botticelli": 1,
    "Giotto di Bondone": 1,
    "Jan van Eyck": 1,
    "El Greco": 1,
    "Peter Paul Rubens": 1,
    "Vincent van Gogh": 1,
    "Claude Monet": 1,
    "Edgar Degas": 1,
    "Edouard Manet": 1,
    "Pierre-Auguste Renoir": 1,
    "Georges Seurat": 1,
    "Henri Matisse": 1,
    "Paul Cézanne": 1,
    "Paul Gauguin": 1,
    "Henri de Toulouse-Lautrec": 1,
    "Marc Chagall": 1,
    "Gustav Klimt": 1,
    "Amedeo Modigliani": 1,
    "Pablo Picasso": 1,
    "Frida Kahlo": 1,
    "Diego Rivera": 1,
    "Jackson Pollock": 1,
    "Willem de Kooning": 1,
    "Edvard Munch": 1,
    "Kazimir Malevich": 1,
    "Gustave Courbet": 1,
    "William Turner": 1,
    "John Singer Sargent": 1,
    "James Whistler": 1,
    "Mary Cassatt": 1,
    "Camille Pissarro": 1,
}


random_artist = random.choice(list(artists))
random_dead_artist = random.choice(list(dead_artists))

subject = "anthropomorphic wolf"
backgrounds = {
    "psychedelic background": 1,
    "vintage background": 2,
    "art nouveau background": 1,
    "fantasy landscape": 3,
    "abstract background": 2,
    "sci-fi backdrop": 1,
}
colors = {
    "psychedelic colors": 2,
    "vibrant colors": 3,
    "vintage colors": 2,
    "pastel colors": 1,
    "earth tones": 2,
    "monochromatic colors": 1,
    "neon colors": 2,
}
styles = {
    "concept art": 7,
    "drawing": 4,
    "photo": 34,
    "digital art": 4,
    "watercolor": 15,
    "comic book": 5,
    "realistic painting": 13,
    "anime": 1,
}
lighting_tags = {
    "cinematic lighting": 12,
    "natural lighting": 2,
    "mood lighting": 12,
    "ambient lighting": 12,
    "neon lighting": 1,
    "candlelight": 1,
    "underwater lighting": 1,
}
qualities = {
    "seamless": 2,
    "ornament": 1,
    "8k": 1,
    "unreal engine 5": 2,
    "ray tracing": 2,
    "unreal engine render": 1,
    "hyper-realistic": 3,
    "realistic": 2,
    "3d": 2,
    "cycles render": 1,
}

# Weighted random selections
def weighted_random_choice(options):
    total_weight = sum(options.values())
    rand = random.uniform(0, total_weight)
    current_weight = 0
    for key, weight in options.items():
        current_weight += weight
        if rand <= current_weight:
            return key

# Define possible species with their corresponding weights
species = [
    ("wolf", 5),
    ("🐺", 1)
]

# List of possible adjectives with weights
adjectives = [
    ("fierce", 2),
    ("majestic", 3),
    ("playful", 2),
    ("mysterious", 2)
]

# List of possible variants with weights
variants = [
    ("anthropomorphic", 1),
    ("wild", 2),
    ("fantasy", 1)
]

# Randomly choose whether to include an adjective and variant
include_adjective = random.choices([True, False], [2, 1])[0]
include_variant = random.choices([True, False], [2, 1])[0]

# Randomly choose a species based on weights
random_species = random.choices(*zip(*species))[0]

# Randomly choose an adjective based on weights
random_adjective = random.choices(*zip(*adjectives))[0] if include_adjective else ""

# Randomly choose a variant based on weights
random_variant = random.choices(*zip(*variants))[0] if include_variant else ""

# Initialize the subject with the selected species
subject = random_species

# Add an adjective if selected
if include_adjective:
    subject = f"{random_adjective} {subject}"

# Add a variant if selected
if include_variant:
    subject = f"{random_variant} {subject}"

random_background = weighted_random_choice(backgrounds)
random_style = weighted_random_choice(styles)
random_color = weighted_random_choice(colors)
random_lighting = weighted_random_choice(lighting_tags)
random_qualities = random.sample(list(qualities), 2)
first_quality, second_quality = random_qualities

# Print the generated text
output_text = f"{subject}, {random_background}, {random_color}, {random_style}, {random_lighting}, {first_quality}, {second_quality}, art by {random_artist} and {random_dead_artist}"

print(output_text)
pyperclip.copy(output_text)
