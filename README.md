# Challenge final

 This repo uses `python 3.10` and `uv` as a python dependency manager.
 
Simply install `uv` and run 
```commandline
uv sync
```

And you're all set.

## Run the streamlit server 

```commandline
uv run streamlit app/main.py
```

## Run the label-studio server

### Export the environment variables (for local storage sync) : 

```commandline
 export LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
 export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=/home/yacineh
```

(see [the label-studio guide on storage](https://labelstud.io/guide/storage) for more info) 

### And run the label-studio server

```commandline
uv run label-studio start
```