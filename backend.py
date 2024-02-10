import csv
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def create_emotion_pie_chart(csv_file):
    emotions = {}
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            emotion = row['emotion']
            percentage = int(row['pourcentage_emotion'])
            if emotion in emotions:
                emotions[emotion] += percentage
            else:
                emotions[emotion] = percentage

    sizes = list(emotions.values())

    # Set the backend to 'Agg' explicitly
    plt.switch_backend('Agg')

    fig1, ax1 = plt.subplots()
    patches, texts, _ = ax1.pie(sizes, autopct='%1.1f%%', startangle=90)

    # Ajout de l'annotation de l'émotion et de son pourcentage
    annotations = []

    plt.legend(patches, annotations, loc="best", bbox_to_anchor=(1, 0.5))

    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    # plt.title('Pourcentages des émotions')

    # Save the plot to a BytesIO buffer and convert to base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return image_base64

# Example usage
image_base64 = create_emotion_pie_chart('merged_output.csv')
print(image_base64)  # You can use this base64 string in your web application



# Exemple d'utilisation :
image_base64 = create_emotion_pie_chart('merged_output.csv')
print(image_base64)  # You can use this base64 string in your web application


def analyze_emotions(csv_file):
    emotions = {}

    # Calculating total percentages for each emotion
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            emotion = row['emotion']
            percentage = int(row['pourcentage_emotion'])
            if emotion in emotions:
                emotions[emotion] += percentage
            else:
                emotions[emotion] = percentage

    # Finding the emotion with the highest percentage
    max_emotion = max(emotions, key=emotions.get)
    max_percentage = emotions[max_emotion]

    # Providing recommendations for the emotion with the highest percentage
    recommendations = []
    if max_emotion == 'fear':
        recommendations.extend([
            "Offer reassurance and clarity in instructions.",
            "Encourage open communication and address concerns promptly.",
            "Provide supportive resources for managing anxiety."
        ])
    elif max_emotion == 'sad':
        recommendations.extend([
            "Create opportunities for students to express their feelings.",
            "Offer additional support through counseling or guidance services."
        ])
    elif max_emotion == 'neutral':
        recommendations.extend([
            "Explore ways to increase engagement through interactive activities.",
            "Encourage participation and discussion to foster a sense of community."
        ])
    elif max_emotion == 'angry':
        recommendations.extend([
            "Address potential triggers and conflicts with empathy and understanding.",
            "Provide channels for expressing grievances and resolving conflicts."
        ])
    elif max_emotion == 'happy':
        recommendations.extend([
            "Acknowledge and celebrate student achievements and successes.",
            "Foster a positive and inclusive learning environment."
        ])
    elif max_emotion == 'surprise':
        recommendations.extend([
            "Clarify expectations and communicate any changes in course content.",
            "Encourage adaptability and openness to new learning experiences."
        ])
    elif max_emotion == 'disgust':
        recommendations.extend([
            "Evaluate and address any issues causing discomfort or dissatisfaction.",
            "Provide alternative resources or options for sensitive topics."
        ])

    return max_emotion.capitalize(), recommendations


# Example usage
emotion, recommendations = analyze_emotions('merged_output.csv')
print(f"Emotion with highest percentage: {emotion}")
print("Recommendations:")
for recommendation in recommendations:
    print("-", recommendation)
#------------------------------------------------------------------------------
def plot_engagement_percentage(csv_file):
    engagements = {'Engaged': 0, 'Not Engaged': 0}

    # Calculating total engagement percentages
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            engagement = row['niveau_dengagement']
            if engagement in engagements:
                engagements[engagement] += 1

    # Plotting engagement percentages
    labels = list(engagements.keys())
    sizes = list(engagements.values())

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Pourcentage d\'engagement')

    # Save the plot to a BytesIO buffer and convert to base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return image_base64

# Example usage
image_base64 = plot_engagement_percentage('merged_output.csv')
print(image_base64)  # You can use this base64 string in your web application

#--------------------------------------------------------------------------------------------
import csv

def analyze_engagement(csv_file):
    engagements = {'Engaged': 0, 'Not Engaged': 0}

    # Calculating total engagement percentages
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            engagement = row['niveau_dengagement']
            if engagement in engagements:
                engagements[engagement] += 1

    # Getting engagement percentages
    total_students = sum(engagements.values())
    engaged_percentage = (engagements['Engaged'] / total_students) * 100
    not_engaged_percentage = (engagements['Not Engaged'] / total_students) * 100

    # Providing recommendations based on engagement percentages
    if engaged_percentage > not_engaged_percentage:
        recommendations = [
            "Encourage active participation through interactive activities and discussions.",
            "Provide regular feedback to reinforce engagement and motivation.",
            "Offer additional support and resources to students facing challenges."
        ]
    elif engaged_percentage < not_engaged_percentage:
        recommendations = [
            "Identify factors contributing to disengagement and address them proactively.",
            "Vary teaching methods to capture students' interest and encourage participation.",
            "Create an inclusive learning environment where all students feel valued and supported."
        ]
    else:
        recommendations = [
            "Foster open communication to address students' concerns and needs.",
            "Adapt course content and activities to cater to students' interests and learning styles.",
            "Provide opportunities for collaboration and peer interaction."
        ]

    return recommendations

# Example usage
recommendations = analyze_engagement('merged_output.csv')
for recommendation in recommendations:
    print("-", recommendation)
