ALTER TABLE countries
    ADD CONSTRAINT fk_countries_currency_code
        FOREIGN KEY (currency_code)
            REFERENCES currencies(currency_code)
                ON DELETE CASCADE,
    ADD CONSTRAINT fk_countries_continent_code
        FOREIGN KEY (continent_code)
            REFERENCES continents(continent_code)
                ON DELETE CASCADE;