def model_to_json():
    from tensorflow.keras.models import load_model # type: ignore
    import json

    # Load the model
    model = load_model("14_DL_Simple_RNN/simple_rnn_imdb.h5", compile=False)

    # Get the model configuration as JSON
    config = model.to_json()

    # Save it to inspect
    with open("model_config.json", "w") as f:
        f.write(config)

    print("Model config saved. Check model_config.json for 'time_major'.")


def json_to_model():
    import json
    # Load the modified JSON config
    with open("model_config.json", "r") as f:
        config = json.load(f)

    # Recreate the model without 'time_major'
    from tensorflow.keras.models import model_from_json # type: ignore

    new_model = model_from_json(json.dumps(config))
    new_model.save("fixed_model.h5")

json_to_model()