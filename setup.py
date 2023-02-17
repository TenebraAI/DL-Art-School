import setuptools

from pip.req import parse_requirements

with open("README.old.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DL-Art-School",
    packages=setuptools.find_packages(),
    version="0.0.1",
    author="James Betker",
    author_email="james@adamant.ai",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.ecker.tech/mrq/DL-Art-School",
    project_urls={},
    scripts=[],
    include_package_data=True,
    install_requires=[
        # Fundamentals
        "numpy",
        "pyyaml",
        "tb-nightly",
        "future",
        "scp",
        "tqdm",
        "matplotlib",
        "scipy",
        "munch",
        "tqdm",
        "scp",
        "tensorboard",
        "orjson",
        "einops",
        "lambda-networks",
        "mup",

        # For image generation stuff
        "opencv-python",
        "kornia",
        "pytorch_ssim",
        "gsa-pytorch",
        "pytorch_fid",

        # For audio generation stuff
        "inflect",
        "librosa",
        "Unidecode",
        "tgt",
        "pyworld",
        "audio2numpy",
        "SoundFile",

        # For text stuff
        "transformers",
        "tokenizers",
        "jiwer",  # calculating WER
        "omegaconf",

        # lucidrains stuff
        "vector_quantize_pytorch",
        "linear_attention_transformer",
        "rotary-embedding-torch",
        "axial_positional_embedding",
        "g-mlp-pytorch",
        "x-clip",
        "x_transformers==1.0.4",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
