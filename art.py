import random
import pyperclip
from datetime import datetime

# Define possible species, adjectives, and franchises as sets and whatever that is..
species = {
    # "wolf", 2000       # Wolves are preferred
    # "🐺", 1000         # Wolf emojis are ok sometimes
    "raccoon": 10,     # Raccoons are favored
    "🦝": 15,          # Raccoon emoji
    "fox": 10,         # Foxes are favored
    "🦊": 15,          # Fox emoji
    "tiger": 5,        # Tigers are favored
    "🐯": 10,          # Tiger emoji
    "lion": 5,         # Lions are favored
    "🦁": 10,          # Lion emoji
    "cheetah": 5,      # Cheetahs are favored
    "🐆": 10,          # Cheetah emoji
    "panther": 5,      # Panthers are favored
    "jaguar": 5,       # Jaguars are favored
    "leopard": 5,      # Leopards are favored
    "bat": 10,         # Bats are favored
    "🦇": 20,          # Bat emoji
    "spider": 10,      # Spiders are favored
    "🕷️": 20,          # Spider emoji
    "snake": 10,       # Snakes are favored
    "🐍": 20,          # Snake emoji
    "owl": 10,         # Owls are favored
    "hawk": 10,        # Hawks are favored
    "falcon": 10,      # Falcons are favored
    "eagle": 10        # Eagles are favored
}

species = {
    "terence mckenna": 1
}

adjectives = {
    "wild": 200,
    "fantasy": 200,
    "realistic": 100,
    "psychedelic": 60,
    "abstract": 50,
    "sci-fi": 50,
    "surreal": 25,
    "minimalistic": 10,
    "steampunk": 50,
    "cyberpunk": 50,
    "mystical": 100,
    "vintage": 20,
    "modern": 10,
    "digital": 10,
    "fierce": 1,
    "majestic": 1,
    "playful": 1,
    "mysterious": 1,
    "gothic": 2,
}

adjectives = {
    "sci-fi": 1,
    "cyberpunk": 1
}

franchises = {
    "from the vampire the masquerade": 3,
    "from bloodborne": 10,
    "from dark souls": 10,
    "from castlevania": 10,
    "from sekiro": 10,
    "from hollow knight": 10,
    "from the witcher 3": 10,
    "from resident evil": 10,
    "from the silent hill": 10,
    "from amnesia dark descent": 10,
    "from the order: 1886": 10,
    "from bloodborne kart": 10,
    "from remnant: From the Ashes": 10,
    "from elden ring": 1,
}

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

# Current year unfolds,
# Time's passage, story untold,
# A year's tale, behold.
current_year = datetime.now().year

# Dead artists with weight,
# Time elapsed, poetic fate,
# Eternal debate.
dead_artists = {
    "Leonardo da Vinci": current_year - 1519,
    "Michelangelo Buonarroti": current_year - 1564,
    "Raphael": current_year - 1520,
    "Caravaggio": current_year - 1610,
    "Rembrandt van Rijn": current_year - 1669,
    "Vermeer": current_year - 1675,
    "Titian": current_year - 1576,
    "Hieronymus Bosch": current_year - 1516,
    "Pieter Bruegel the Elder": current_year - 1569,
    "Sandro Botticelli": current_year - 1510,
    "Giotto di Bondone": current_year - 1337,
    "Jan van Eyck": current_year - 1441,
    "El Greco": current_year - 1614,
    "Peter Paul Rubens": current_year - 1640,
    "Vincent van Gogh": current_year - 1890,
    "Claude Monet": current_year - 1926,
    "Edgar Degas": current_year - 1917,
    "Edouard Manet": current_year - 1883,
    "Pierre-Auguste Renoir": current_year - 1919,
    "Georges Seurat": current_year - 1891,
    "Henri Matisse": current_year - 1954,
    "Paul Cézanne": current_year - 1906,
    "Paul Gauguin": current_year - 1903,
    "Henri de Toulouse-Lautrec": current_year - 1901,
    "Marc Chagall": current_year - 1985,
    "Gustav Klimt": current_year - 1918,
    "Amedeo Modigliani": current_year - 1920,
    "Frida Kahlo": current_year - 1954,
    "Diego Rivera": current_year - 1957,
    "Jackson Pollock": current_year - 1956,
    "Willem de Kooning": current_year - 1997,
    "Edvard Munch": current_year - 1944,
    "Kazimir Malevich": current_year - 1935,
    "Gustave Courbet": current_year - 1877,
    "William Turner": current_year - 1851,
    "John Singer Sargent": current_year - 1925,
    "James Whistler": current_year - 1903,
    "Mary Cassatt": current_year - 1926,
    "Camille Pissarro": current_year - 1903,
    "Jean Dubuffet": current_year - 1985,
    "Yves Klein": current_year - 1962,
    "Philip Guston": current_year - 1980,
    "Ad Reinhardt": current_year - 1967,
    "Wassily Kandinsky": current_year - 1944,
    "Giacomo Balla": current_year - 1958,
    "Tarsila do Amaral": current_year - 1973,
    "Paul Klee": current_year - 1940,
    "Hans Hofmann": current_year - 1966,
    "Piet Mondrian": current_year - 1944,
    "Joan Miró": current_year - 1983,
    "Georgia O'Keeffe": current_year - 1986,
    "Edward Hopper": current_year - 1967,
    "Max Ernst": current_year - 1976,
    "Amedeo Modigliani": current_year - 1920,
    "Pablo Picasso": current_year - 1973,
    "H.R. Giger": current_year - 2014,
    "Frank Frazetta": current_year - 2010,
    "Boris Vallejo": current_year - 2022,
    "Luis Royo": current_year - 2021,
    "Moebius": current_year - 2012,
    "Wayne Barlowe": current_year - 2020,
    "Don Maitz": current_year - 2021,
    "Jill Bauman": current_year - 2020,
    "Michael Whelan": current_year - 2022,
    "Rowena Morrill": current_year - 2021,
    "Brom": current_year - 2022,
    "Stephan Martiniere": current_year - 2022,
}

backgrounds = {
    "psychedelic background": 1,
    "vintage background": 2,
    "art nouveau background": 1,
    "victorian background": 3,
    "steampunk background": 2,
    "gothic background": 2,
    "vampire the masquerade": 3,
    "fantasy landscape": 3,
    "abstract background": 2,
    "sci-fi backdrop": 1,
    "surreal dreamscape": 3,
    "steampunk setting": 2,
    "cyberpunk cityscape": 2,
    "magical forest": 3,
    "underwater abyss": 2,
}

colors = {
    "psychedelic colors": 2,
    "vibrant colors": 3,
    "vintage colors": 2,
    "pastel colors": 1,
    "earth tones": 2,
    "monochromatic colors": 1,
    "neon colors": 2,
    "mystical hues": 3,
    "ethereal shades": 2,
    "candy-coated palette": 4,
    "gloomy tints": 4,
    "celestial colors": 3,
    "whimsical shades": 5,
    "dreamy gradients": 5,
    "funky pigments": 5,
    "jazzy tones": 5,
    "enchanted spectrum": 5,
    "extraterrestrial hues": 5,
    "hypnotic tints": 5,
    "surrealistic shades": 5,
    "psychochromatic palette": 5,
    "vivid hallucinations": 5,
    "otherworldly colors": 5,
    "vortex of pigments": 5,
    "phantasmagoric shades": 5,
    "mind-bending hues": 5,
    "chaotic color explosion": 5,
    "whimsical wonderland": 5,
    "absurdly vivid spectrum": 5
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
    "impressionist brushwork": 3,
    "minimalist design": 2,
    "abstract expressionism": 4,
    "vintage illustration": 3,
    "surrealism": 4,
}

lighting_tags = {
    "cinematic lighting": 12,
    "natural lighting": 2,
    "mood lighting": 12,
    "ambient lighting": 12,
    "neon lighting": 1,
    "candlelight": 1,
    "underwater lighting": 1,
    "ethereal radiance": 3,
    "shadowplay": 2,
    "twilight glow": 2,
    "starry night": 3,
    "mystic aura": 3,
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
    "immaculate detail": 3,
    "masterful craftsmanship": 2,
    "intricate precision": 2,
    "awe-inspiring scale": 3,
}

articles = [
    ("rocky mountains in the background, ", 5),
    ("snowy mountains in the background, ", 5),
    ("ancient civilizations in ruins, ", 5),
    ("towering waterfalls in the backdrop, ", 5),
    ("mysterious caves hidden in darkness, ", 5),
    ("volcanic eruptions spewing molten lava, ", 5),
    ("a tranquil pond with lily pads, ", 5),
    ("lush vine-covered jungles, ", 5),
    ("mystical fog enveloping enchanted forests, ", 5),
    ("majestic temples against a fiery sunset, ", 5),
    ("underwater kingdoms teeming with life, ", 5),
    ("a rainbow arching over emerald valleys, ", 5),
    ("crystal-clear lakes surrounded by mountains, ", 5),
    ("enchanted waterfalls with cascading waters, ", 5),
    ("haunted mansions beneath a full moon, ", 5),
    ("frozen tundras under the northern lights, ", 5),
    ("magical portals to distant realms, ", 5),
    ("timeless castles amidst rolling hills, ", 5),
    ("a celestial sky filled with shooting stars, ", 5),
    ("ancient libraries with towering bookshelves, ", 5),
    ("serene cherry blossom gardens, ", 5),
    ("underground caverns with glowing crystals, ", 5),
    ("fiery dragons soaring through the skies, ", 5),
    ("enchanted waterfalls with hidden caves, ", 5),
    ("floating islands in a sea of clouds, ", 5),
    ("steampunk airships soaring above the city, ", 5),
    ("mystical creatures roaming enchanted forests, ", 5),
    ("magical gardens with talking flowers, ", 5),
    ("underwater shipwrecks with hidden treasures, ", 5),
    ("ancient wizards' towers with arcane symbols, ", 5),
    ("lush oases in the midst of the desert, ", 5),
    ("futuristic space stations in distant galaxies, ", 5),
    ("lush green forests in the distance, ", 5),
    ("a serene river flowing gently, ", 5),
    ("ancient ruins under a setting sun, ", 5),
    ("a picturesque village by the sea, ", 5),
    ("rolling hills covered in wildflowers, ", 5),
    ("towering cathedrals in the cityscape, ", 5),
    ("a peaceful countryside with windmills, ", 5),
    ("mystical castles amidst fog, ", 5),
    ("dramatic cliffs by the coastline, ", 5),
    ("vast deserts under a starry night, ", 5),
    ("a tranquil meadow with grazing animals, ", 5),
    ("dense jungles teeming with wildlife, ", 5),
    ("ancient temples hidden in the jungle, ", 5),
    ("moonlit beaches with crashing waves, ", 5),
    ("vibrant coral reefs in crystal clear waters, ", 5),
    ("cosmic nebulae in the night sky, ", 5),
    ("alien landscapes on distant planets, ", 5),
    ("enchanting forests with glowing mushrooms, ", 5),
    ("ancient pyramids beneath the desert sands, ", 5),
    ("futuristic cityscapes with flying cars, ", 5),
    ("enchanted forests with talking animals, ", 5),
    ("mythical creatures in enchanted groves, ", 5),
    ("floating islands among the clouds, ", 5),
    ("surreal dreamscapes with melting clocks, ", 5),
    ("magical realms with floating castles, ", 5),
    ("fantasy kingdoms under double rainbows, ", 5),
    ("otherworldly dimensions with bizarre flora, ", 5),
    #("a ", 30),
    #("an ", 30),
    #("", 10),
    #("photo of ", 10),
    #("photo of an ", 10),
    #("photo of a ", 10),
    #("a beautiful photo photo of ", 10),
    #("a beautiful photo photo of an ", 10),
    #("a beautiful photo photo of a ", 10),
    #("a beautiful image of ", 10),
    #("a beautiful image of an ", 10),
    #("a beautiful image of a", 10),
    #("an image of ", 10),
    #("a image of ", 10),
    #("an image of a ", 5),
    #("an image of an ", 5),
    #("the ", 10),
    #("this ", 5),
    #("some ", 5),
    #("my ", 5),
    #("your ", 5),
    #("our ", 5),
    #("their ", 5),
    #("that ", 5),
    #("these ", 5),
    #("those ", 5),
    #("every ", 5),
    #("another ", 5),
    #("several ", 5),
    #("many ", 5),
    #("more ", 5),
    #("few ", 5),
    #("one ", 5),
    #("two ", 5),
    #("three ", 5),
    #("four ", 5),
    #("five ", 5),
    #("my little ", 1),
    #("a new ", 5),
    #("the big ", 5),
    #("your favorite ", 5),
    #("some old ", 5),
    #("an interesting ", 5),
    #("another exciting ", 5),
    #("this mysterious ", 15),
    #("a giant ", 51),
    #("the tiny ", 51),
    #("their colorful ", 35),
    #("everyday ", 5),
    #("any peculiar ", 5),
    #("several shiny ", 35),
    #("many ancient ", 5),
    #("more delicious ", 30),
    #("few hidden ", 15),
    #("one magical ", 5),
    #("two mysterious ", 5),
    #("three musical ", 25),
    #("four futuristic ", 35),
    #("five incredible ", 45),
]

# Weighted random selections


def weighted_random_choice(options):
    total_weight = sum(options.values())
    rand = random.uniform(0, total_weight)
    current_weight = 0
    for key, weight in options.items():
        current_weight += weight
        if rand <= current_weight:
            return key


random_artist = random.choice(list(artists))
random_dead_artist = random.choice(list(dead_artists))
# Randomly choose whether to include an adjective and variant
include_adjective = random.choices([True, False], [3, 1])[0]
include_variant = random.choices([True, False], [14, 1])[0]
random_species = random.choice(list(species))
# Randomly choose an adjective based on the set
random_adjective = random.sample(list(adjectives), 1)[
    0] if include_adjective else ""
# Randomly choose a variant based on the set
random_variant = random.sample(list(franchises), 1)[
    0] if include_variant else ""
# Initialize the subject with the selected species
subject = random_species

# Add an adjective if selected
if include_adjective:
    subject = f"{random_adjective}"

# Add a variant if selected
if include_variant:
    subject = f"{random_variant}"

# Randomly choose an article ("a," "an," or nothing) based on weights
article = weighted_random_choice(dict(articles))

# Choose a random background style based on weights
random_background = weighted_random_choice(backgrounds)
# Choose a random art style based on weights
random_style = weighted_random_choice(styles)
# Choose a random color scheme based on weights
random_color = weighted_random_choice(colors)
# Choose a random lighting style based on weights
random_lighting = weighted_random_choice(lighting_tags)
# Sample two random qualities from the list
random_qualities = random.sample(list(qualities), 2)
first_quality, second_quality = random_qualities

# Randomly choose an artist and a dead artist
random_artist = weighted_random_choice(artists)
random_dead_artist = weighted_random_choice(dead_artists)

# Generate the prompt.
prompt = f"{article}anthropomorphic {random_species}, {subject}, {random_background}, {random_color}, sublime {random_style}, {random_lighting}, {first_quality}, {second_quality}, art by {random_artist} and {random_dead_artist}"

print(prompt)
# Copy prompt to clipboard.
pyperclip.copy(prompt)
