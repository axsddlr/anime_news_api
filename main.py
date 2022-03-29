import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.anime_sources import Ani

from ratelimit import limits

app = FastAPI(
    title="Unofficial Anime News API",
    description="An Unofficial REST API for various anime news websites, Made by [Andre "
                "Saddler]( "
                "https://github.com/axsddlr)",
    version="1.0.0",
    docs_url="/",
    redoc_url=None,
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# init classes
anime = Ani()

TWO_MINUTES = 150


@limits(calls=250, period=TWO_MINUTES)
@app.get("/ann", tags=["News"])
def anime_network_news():
    """
    """
    return anime.get_ann_entires()


@limits(calls=250, period=TWO_MINUTES)
@app.get("/mal", tags=["News"])
def my_anime_list_news():
    """
    News and Updates
    """
    return anime.get_mal_entires()


@limits(calls=250, period=TWO_MINUTES)
@app.get("/crunchyroll", tags=["News"])
def crunchyroll_anime_news():
    """
    News and Updates
    """
    return anime.get_crunchy_entires()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3000)
