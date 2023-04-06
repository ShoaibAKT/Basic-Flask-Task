from flask import Flask, render_template,redirect,url_for

class ML:
    def __init__(self):
        self.avaliable_models = {
            "face_detection": "/additional_drive/ML/face_detection",
            "car_detection": "/additional_drive/ML/car_detection",
            "shoe_detection": "/additional_drive/ML/shoe_detection",
            "cloth_detection": "/additional_drive/ML/cloth_detection",
            "signal_detection": "/additional_drive/ML/signal_detection",
            "water_level_detection": "/additional_drive/ML/water_level_detection",
            "missile_detection": "/additional_drive/ML/missile_detection"
        }
        self.loaded_models_limit = 2
        self.loaded_models = {
            model: self.load_weights(model)
            for model in list(self.avaliable_models)[:self.loaded_models_limit]
        }
        self.requests_count = {model: 0 for model in self.loaded_models}

    def load_weights(self, model):
        return self.avaliable_models.get(model, None)

    def load_balancer(self, new_model):
        least_used_model = min(self.requests_count, key=self.requests_count.get)
        del self.loaded_models[least_used_model]
        self.loaded_models[new_model] = self.load_weights(new_model)

app = Flask(__name__)
ml = ML()

@app.route('/get_loaded_models', methods=['GET', 'POST'])
def get_loaded_models():
    return render_template('loaded_models.html', models=ml.loaded_models)

@app.route('/process_request', methods=['GET', 'POST'])
def process_request():
    try:
        model = request.form["model"]
        if model not in ml.loaded_models:
            ml.load_balancer(model)
        ml.requests_count[model] += 1
        return "processed by "+ ml.loaded_models[model]
    except:
        return str(traceback.format_exc())

app.run()