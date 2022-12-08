from stability_sdk.client import StabilityInference,process_artifacts_from_answers

# Set up logging for output to console.
def generate(prompt: str):

    STABILITY_KEY: str = "sk-aAoGq2gCMVrxLTeSWcNxcax5mjK3fH9XHIOm6NS73GOzsSnb"
    STABILITY_HOST = "grpc.stability.ai:443"

    request =  {
        "height": 512,
        "width": 512,
        "start_schedule":0.5, 
        "end_schedule": 0.01,
        "cfg_scale": 7.0,                
        "seed": 0,
        "samples": 1,
        "init_image": None,
        "mask_image": None,
        "steps": 15,
    }
    engine = "stable-diffusion-v1-5"
    prefix = "generation_"

    stability_api = StabilityInference(
        STABILITY_HOST, STABILITY_KEY, engine=engine, verbose=True
    )

    answers = stability_api.generate(prompt, **request)
    artifacts = process_artifacts_from_answers(
        prefix, prompt, answers, write=True, verbose=True
    )