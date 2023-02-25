-- Create a table for 'google_play_store'
DROP TABLE IF EXISTS google_play_store;
CREATE TABLE google_play_store (
    "App" VARCHAR NOT NULL,
    "Category" VARCHAR NOT NULL,
    "Rating" FLOAT NOT NULL,
    "Reviews" INT NOT NULL,
    "Size" VARCHAR NOT NULL,
    "Installs" VARCHAR NOT NULL,
    "Type" VARCHAR NOT NULL,
    "Price" VARCHAR NOT NULL,
    "Content Rating" VARCHAR NOT NULL,
    "Genres" VARCHAR NOT NULL,
	PRIMARY KEY ("App")
);
-- Create a table for 'average_category_rating'
DROP TABLE IF EXISTS average_category_rating;
CREATE TABLE average_category_rating (
    "Category" VARCHAR NOT NULL,
    "Rating" FLOAT NOT NULL,
    PRIMARY KEY ("Category")
);
-- Create a table for 'max_reviews'
DROP TABLE IF EXISTS max_reviews;
CREATE TABLE max_reviews (
    "App" VARCHAR NOT NULL,
    "Reviews" INT NOT NULL,
    PRIMARY KEY ("App")
);
-- Create a table for 'average_type_rating'
DROP TABLE IF EXISTS average_type_rating;
CREATE TABLE average_type_rating (
    "Type" VARCHAR NOT NULL,
    "Rating" FLOAT NOT NULL,
    PRIMARY KEY ("Type")
);

ALTER TABLE "google_play_store" ADD CONSTRAINT "Category" FOREIGN KEY("Category")
REFERENCES "average_category_rating" ("Category");

ALTER TABLE "google_play_store" ADD CONSTRAINT "Type" FOREIGN KEY("Type")
REFERENCES "average_type_rating" ("Type");

select * from google_play_store;
select * from average_category_rating;
select * from max_reviews;
select * from average_type_rating;

