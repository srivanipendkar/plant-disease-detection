"""
Disease information database for the Plant Disease Detection app.

Each entry provides:
  - description: a one-line explanation of the disease/condition
  - treatment: general, widely-known treatment/management guidance

Note: This is general agricultural guidance, not a substitute for advice from
a local agricultural extension officer or agronomist, who can account for
your specific crop, region, and severity.
"""

DISEASE_INFO = {
    "Pepper__bell___Bacterial_spot": {
        "description": "A bacterial infection causing dark, water-soaked spots on leaves and fruit, which can lead to leaf drop.",
        "treatment": "Remove and destroy infected plant debris; apply copper-based bactericides; avoid overhead watering to reduce spread.",
    },
    "Pepper__bell___healthy": {
        "description": "The leaf shows no signs of disease.",
        "treatment": "No treatment needed. Continue regular monitoring and good field hygiene.",
    },
    "Potato___Early_blight": {
        "description": "A fungal disease causing dark, concentric-ringed spots on older leaves, reducing yield if untreated.",
        "treatment": "Apply fungicides containing chlorothalonil or mancozeb; rotate crops; remove infected foliage.",
    },
    "Potato___Late_blight": {
        "description": "A fast-spreading fungal-like disease causing dark, greasy lesions that can destroy a crop within days.",
        "treatment": "Apply fungicides with chlorothalonil or copper-based compounds immediately; destroy infected plants to prevent spread; avoid overhead irrigation.",
    },
    "Potato___healthy": {
        "description": "The leaf shows no signs of disease.",
        "treatment": "No treatment needed. Continue regular monitoring and good field hygiene.",
    },
    "Tomato_Bacterial_spot": {
        "description": "A bacterial disease causing small, dark, water-soaked spots on leaves and fruit.",
        "treatment": "Apply copper-based bactericides; avoid working with wet plants; use disease-free seeds and resistant varieties.",
    },
    "Tomato_Early_blight": {
        "description": "A fungal disease producing dark spots with concentric rings, usually starting on lower/older leaves.",
        "treatment": "Apply fungicides (chlorothalonil, mancozeb); remove affected lower leaves; ensure good air circulation between plants.",
    },
    "Tomato_Late_blight": {
        "description": "An aggressive disease causing large, irregular, water-soaked lesions that can rapidly destroy the plant.",
        "treatment": "Apply fungicides promptly (chlorothalonil, copper-based); remove and destroy infected plants; avoid overhead watering.",
    },
    "Tomato_Leaf_Mold": {
        "description": "A fungal disease causing pale spots on the upper leaf surface and olive-green mold underneath, common in humid conditions.",
        "treatment": "Improve ventilation and reduce humidity; apply fungicides if severe; avoid wetting foliage during watering.",
    },
    "Tomato_Septoria_leaf_spot": {
        "description": "A fungal disease causing small, circular spots with dark borders and light centers on lower leaves.",
        "treatment": "Remove infected leaves; apply fungicides (chlorothalonil, copper-based); rotate crops and avoid overhead watering.",
    },
    "Tomato_Spider_mites_Two_spotted_spider_mite": {
        "description": "Tiny pests causing stippled, discolored leaves and fine webbing, thriving in hot, dry conditions.",
        "treatment": "Apply miticides or insecticidal soap; increase humidity around plants; introduce natural predators like ladybugs where possible.",
    },
    "Tomato__Target_Spot": {
        "description": "A fungal disease causing brown spots with concentric rings, often starting on older leaves.",
        "treatment": "Apply fungicides (chlorothalonil, mancozeb); improve air circulation; remove infected leaves promptly.",
    },
    "Tomato__Tomato_YellowLeaf__Curl_Virus": {
        "description": "A viral disease spread by whiteflies, causing yellowing, curling, and stunted growth.",
        "treatment": "Control whitefly populations with insecticides or sticky traps; remove and destroy infected plants; use resistant varieties where available.",
    },
    "Tomato__Tomato_mosaic_virus": {
        "description": "A viral disease causing mottled light and dark green patterns on leaves, with stunted growth.",
        "treatment": "No chemical cure — remove and destroy infected plants; disinfect tools between use; control aphids which can spread the virus.",
    },
    "Tomato_healthy": {
        "description": "The leaf shows no signs of disease.",
        "treatment": "No treatment needed. Continue regular monitoring and good field hygiene.",
    },
}


def get_disease_info(class_name: str) -> dict:
    """Look up disease info, with a safe fallback if a class isn't in the database."""
    return DISEASE_INFO.get(
        class_name,
        {
            "description": "Detailed information for this class is not yet available.",
            "treatment": "Consult a local agricultural extension officer for diagnosis confirmation and treatment options.",
        },
    )
