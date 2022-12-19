from stability_sdk.client import StabilityInference,process_artifacts_from_answers
import time
import zlib

# Set up logging for output to console.
def generate(prompt: str, width: int = 512,
             height: int = 512, step:int = 30, engine: str = "stable-diffusion-v1-5"):

    STABILITY_KEY: str = "sk-aAoGq2gCMVrxLTeSWcNxcax5mjK3fH9XHIOm6NS73GOzsSnb"
    STABILITY_HOST = "grpc.stability.ai:443"

    request =  {
        "height": height,
        "width": width,
        "start_schedule":0.5, 
        "end_schedule": 0.01,
        "cfg_scale": 7.0,                
        "seed": 0,
        "samples": 1,
        "init_image": None,
        "mask_image": None,
        "steps": step,
    }
    prefix = "/opt/work/draw_world_img/"

    stability_api = StabilityInference(
        STABILITY_HOST, STABILITY_KEY, engine=engine, verbose=True
    )
    answers = stability_api.generate(prompt, **request)
    prompt_file_name = str(time.time() * 1000) + str(zlib.crc32(prompt.encode("utf8")))
    artifacts = process_artifacts_from_answers(
        prefix, prompt_file_name, answers, write=True, verbose=True
    )
    for artifact in artifacts:
        img_file = artifact[0]
        print("========generate: prompt: %s, req_params: %s, res: %s" % (prompt, str(request), img_file))
        # print("img_file:",img_file)
        artifact_obj = artifact[1]
        # print("artifact_obj:", artifact_obj)
        return (img_file, artifact_obj)
        
        


if __name__ == "__main__":
    print("start.....")
    prompt = """
    arcane style, Highly detailed portrait of (Geralt) of Rivia, the witcher, yellow eyes, witcher video game, unreal engine, global illumination, radiant light, detailed and intricate environment, 8k, art by artgerm and greg rutkowski and alphonse mucha 
    """
    generate(prompt)

