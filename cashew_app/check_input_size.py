from keras.models import load_model

models = [
    "final_model.keras",
    "mobilenet_model.keras",
    "resnet_model.keras"
]

for m in models:
    print("\nLoading:", m)
    model = load_model(m)
    print("Input shape:", model.input_shape)
