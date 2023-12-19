from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Read  text data or use sample data
text_data = "Flowers, the enchanting and delicate marvels of nature, captivate the human senses with their exquisite beauty and diverse array of colors, shapes, and fragrances. These botanical wonders play a pivotal role in ecosystems, serving as the reproductive organs of flowering plants. Each petal, meticulously crafted by nature's design, unfolds like a unique masterpiece, showcasing the plant's reproductive structures. Flowers not only contribute to the survival of their own species through pollination but also provide essential sustenance for myriad pollinators, including bees, butterflies, and hummingbirds. From the resplendent allure of roses to the cheerful vibrancy of sunflowers, the world of flowers is a tapestry of emotions, symbolizing love, friendship, and even mourning. Cultivated for ornamental purposes, medicinal uses, and culinary delights, flowers have woven themselves into the fabric of human culture throughout history. Beyond their aesthetic appeal, flowers hold symbolic significance in various traditions and celebrations, adding a poetic touch to weddings, festivals, and rituals. In gardens and meadows, flowers stand as nature's living poetry, a testament to the intricate dance between flora and fauna. Truly, the world of flowers is a celebration of life, color, and the enduring beauty that blossoms with each passing season."

# Load a flower-shaped mask image
flower_mask = np.array(Image.open("whiteflower.png"))

# Create a WordCloud object with the flower-shaped mask
wordcloud = WordCloud(width=800, height=800, background_color="white", mask=flower_mask).generate(text_data)

# Display the WordCloud using matplotlib
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)

# Save the WordCloud to an image file
wordcloud.to_file("flower_wordcloud.png")

# Show the WordCloud
plt.show()
