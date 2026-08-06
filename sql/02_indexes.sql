USE tennis_analytics;

CREATE INDEX idx_competition_name
ON competitions(competition_name);

CREATE INDEX idx_category
ON competitions(category_id);

CREATE INDEX idx_gender
ON competitions(gender);

CREATE INDEX idx_type
ON competitions(type);

CREATE INDEX idx_country
ON competitors(country);

CREATE INDEX idx_points
ON rankings(points);

CREATE INDEX idx_rank
ON rankings(rank_position);

CREATE INDEX idx_city
ON venues(city_name);

CREATE INDEX idx_country_venue
ON venues(country_name);