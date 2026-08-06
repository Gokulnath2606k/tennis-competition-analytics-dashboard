# ==========================================================
# HOME PAGE QUERIES
# ==========================================================

HOME_KPI = """
SELECT
    (SELECT COUNT(*) FROM competitions) AS total_competitions,
    (SELECT COUNT(*) FROM competitors) AS total_players,
    (SELECT COUNT(*) FROM venues) AS total_venues,
    (SELECT COUNT(*) FROM categories) AS total_categories,
    (SELECT COUNT(*) FROM complexes) AS total_complexes;
"""

TOP20_PLAYERS = """
SELECT
    r.rank_position,
    c.competitor_name,
    c.country,
    r.points,
    r.competitions_played
FROM rankings r
JOIN competitors c
ON r.competitor_id = c.competitor_id
ORDER BY r.rank_position
LIMIT 20;
"""

PLAYERS_BY_COUNTRY = """
SELECT
    country,
    COUNT(*) AS total_players
FROM competitors
WHERE country IS NOT NULL
GROUP BY country
ORDER BY total_players DESC
LIMIT 10;
"""

VENUES_BY_COUNTRY = """
SELECT
    country_name,
    COUNT(*) AS total_venues
FROM venues
WHERE country_name IS NOT NULL
GROUP BY country_name
ORDER BY total_venues DESC
LIMIT 10;
"""



# =====================================================
# COMPETITION ANALYSIS QUERIES (Dynamic Filters)
# =====================================================

def COMPETITION_BY_CATEGORY(where_clause=""):
    return f"""
    SELECT
        cat.category_name,
        COUNT(*) AS competitions
    FROM competitions c
    JOIN categories cat
        ON c.category_id = cat.category_id
    {where_clause}
    GROUP BY cat.category_name
    ORDER BY competitions DESC;
    """


def COMPETITION_TYPE(where_clause=""):
    return f"""
    SELECT
        c.type,
        COUNT(*) AS competitions
    FROM competitions c
    JOIN categories cat
        ON c.category_id = cat.category_id
    {where_clause}
    GROUP BY c.type
    ORDER BY competitions DESC;
    """


def COMPETITION_GENDER(where_clause=""):
    return f"""
    SELECT
        c.gender,
        COUNT(*) AS competitions
    FROM competitions c
    JOIN categories cat
        ON c.category_id = cat.category_id
    {where_clause}
    GROUP BY c.gender
    ORDER BY competitions DESC;
    """


def CATEGORY_GENDER(where_clause=""):
    return f"""
    SELECT
        cat.category_name,
        c.gender,
        COUNT(*) AS total
    FROM competitions c
    JOIN categories cat
        ON c.category_id = cat.category_id
    {where_clause}
    GROUP BY cat.category_name, c.gender
    ORDER BY cat.category_name;
    """


def CATEGORY_TYPE(where_clause=""):
    return f"""
    SELECT
        cat.category_name,
        c.type,
        COUNT(*) AS total
    FROM competitions c
    JOIN categories cat
        ON c.category_id = cat.category_id
    {where_clause}
    GROUP BY cat.category_name, c.type
    ORDER BY cat.category_name;
    """


def TOP_COMPETITIONS(where_clause=""):
    return f"""
    SELECT
        c.competition_name,
        COUNT(*) AS competitions
    FROM competitions c
    JOIN categories cat
        ON c.category_id = cat.category_id
    {where_clause}
    GROUP BY c.competition_name
    ORDER BY competitions DESC
    LIMIT 20;
    """
# ==========================================================
# PLAYER RANKINGS
# ==========================================================

TOP50_PLAYERS = """
SELECT
    r.rank_position,
    c.competitor_name,
    c.country,
    r.points,
    r.competitions_played
FROM rankings r
JOIN competitors c
ON r.competitor_id = c.competitor_id
ORDER BY r.rank_position
LIMIT 50;
"""

TOP_POINTS = """
SELECT
    c.competitor_name,
    r.points
FROM rankings r
JOIN competitors c
ON r.competitor_id = c.competitor_id
ORDER BY r.points DESC
LIMIT 20;
"""

COUNTRY_RANKINGS = """
SELECT
    c.country,
    COUNT(*) AS players
FROM competitors c
JOIN rankings r
ON c.competitor_id = r.competitor_id
GROUP BY c.country
ORDER BY players DESC
LIMIT 15;
"""

RANK_MOVEMENT = """
SELECT
    movement,
    COUNT(*) AS players
FROM rankings
GROUP BY movement
ORDER BY players DESC;
"""

# ==========================================================
# VENUE ANALYSIS
# ==========================================================

VENUE_COUNTRY = """
SELECT
    country_name,
    COUNT(*) AS venues
FROM venues
GROUP BY country_name
ORDER BY venues DESC;
"""

VENUE_CITY = """
SELECT
    city_name,
    COUNT(*) AS venues
FROM venues
WHERE city_name IS NOT NULL
GROUP BY city_name
ORDER BY venues DESC
LIMIT 20;
"""

COMPLEX_VENUES = """
SELECT
    complex_id,
    COUNT(*) AS venues
FROM venues
GROUP BY complex_id
ORDER BY venues DESC
LIMIT 20;
"""

# ==========================================================
# COUNTRY ANALYSIS
# ==========================================================

PLAYERS_COUNTRY = """
SELECT
    country,
    COUNT(*) AS players
FROM competitors
GROUP BY country
ORDER BY players DESC
LIMIT 20;
"""

COMPETITION_COUNTRY = """
SELECT
    category_name,
    COUNT(*) AS competitions
FROM competitions c
JOIN categories cat
ON c.category_id = cat.category_id
GROUP BY category_name
ORDER BY competitions DESC;
"""

VENUES_COUNTRY = """
SELECT
    country_name,
    COUNT(*) AS venues
FROM venues
GROUP BY country_name
ORDER BY venues DESC
LIMIT 20;
"""


# =====================================================
# COUNTRY ANALYSIS QUERIES (Dynamic)
# =====================================================

def PLAYERS_BY_COUNTRY(where_clause="", top_n=10):
    return f"""
    SELECT
        c.country,
        COUNT(*) AS total_players
    FROM competitors c
    JOIN rankings r
        ON c.competitor_id = r.competitor_id

    {where_clause}

    GROUP BY c.country
    ORDER BY total_players DESC
    LIMIT {top_n};
    """


def VENUES_BY_COUNTRY(country_filter="", top_n=10):

    where = ""

    if country_filter != "All":
        where = f"WHERE country_name = '{country_filter}'"

    return f"""
    SELECT
        country_name,
        COUNT(*) AS total_venues
    FROM venues

    {where}

    GROUP BY country_name
    ORDER BY total_venues DESC
    LIMIT {top_n};
    """


def POINTS_BY_COUNTRY(where_clause="", top_n=10):
    return f"""
    SELECT
        c.country,
        SUM(r.points) AS total_points
    FROM rankings r
    JOIN competitors c
        ON r.competitor_id = c.competitor_id

    {where_clause}

    GROUP BY c.country
    ORDER BY total_points DESC
    LIMIT {top_n};
    """


def AVERAGE_POINTS(where_clause="", top_n=10):
    return f"""
    SELECT
        c.country,
        AVG(r.points) AS avg_points
    FROM rankings r
    JOIN competitors c
        ON r.competitor_id = c.competitor_id

    {where_clause}

    GROUP BY c.country
    ORDER BY avg_points DESC
    LIMIT {top_n};
    """


def TOP_PLAYERS_COUNTRY(where_clause="", top_n=10):
    return f"""
    SELECT
        c.country,
        COUNT(*) AS top_players
    FROM rankings r
    JOIN competitors c
        ON r.competitor_id = c.competitor_id

    {where_clause}
    AND r.rank_position <= 100

    GROUP BY c.country
    ORDER BY top_players DESC
    LIMIT {top_n};
    """


def COUNTRY_DISTRIBUTION(where_clause="", top_n=10):
    return f"""
    SELECT
        c.country,
        COUNT(*) AS players
    FROM competitors c
    JOIN rankings r
        ON c.competitor_id = r.competitor_id

    {where_clause}

    GROUP BY c.country
    ORDER BY players DESC
    LIMIT {top_n};
    """


def TOP_COUNTRIES_BY_POINTS(where_clause="", top_n=15):
    return f"""
    SELECT
        c.country,
        SUM(r.points) AS total_points
    FROM rankings r
    JOIN competitors c
        ON r.competitor_id = c.competitor_id

    {where_clause}

    GROUP BY c.country
    ORDER BY total_points DESC
    LIMIT {top_n};
    """

# player Ranking

# =====================================================
# PLAYER RANKINGS
# =====================================================

# =====================================================
# PLAYER RANKINGS QUERIES (Dynamic Filters)
# =====================================================

def TOP_20_PLAYERS(where_clause=""):
    return f"""
    SELECT
        r.rank_position,
        c.competitor_name,
        c.country,
        r.points,
        r.competitions_played
    FROM rankings r
    JOIN competitors c
        ON r.competitor_id = c.competitor_id

    {where_clause}

    ORDER BY r.rank_position
    LIMIT 20;
    """


def TOP_PLAYERS_POINTS(where_clause=""):
    return f"""
    SELECT
        c.competitor_name,
        c.country,
        r.points
    FROM rankings r
    JOIN competitors c
        ON r.competitor_id = c.competitor_id

    {where_clause}

    ORDER BY r.points DESC
    LIMIT 15;
    """


def TOP_PLAYERS_COMPETITIONS(where_clause=""):
    return f"""
    SELECT
        c.competitor_name,
        c.country,
        r.competitions_played
    FROM rankings r
    JOIN competitors c
        ON r.competitor_id = c.competitor_id

    {where_clause}

    ORDER BY r.competitions_played DESC
    LIMIT 15;
    """


def RANKING_MOVEMENT(where_clause=""):
    return f"""
    SELECT
        r.movement,
        COUNT(*) AS players
    FROM rankings r
    JOIN competitors c
        ON r.competitor_id = c.competitor_id

    {where_clause}

    GROUP BY r.movement
    ORDER BY r.movement;
    """


def POINTS_BY_COUNTRY(where_clause=""):
    return f"""
    SELECT
        c.country,
        SUM(r.points) AS total_points
    FROM rankings r
    JOIN competitors c
        ON r.competitor_id = c.competitor_id

    {where_clause}

    GROUP BY c.country
    ORDER BY total_points DESC
    LIMIT 15;
    """


def AVERAGE_POINTS_COUNTRY(where_clause=""):
    return f"""
    SELECT
        c.country,
        AVG(r.points) AS avg_points
    FROM rankings r
    JOIN competitors c
        ON r.competitor_id = c.competitor_id

    {where_clause}

    GROUP BY c.country
    ORDER BY avg_points DESC
    LIMIT 15;
    """


def TOP10_COUNTRIES(where_clause=""):
    return f"""
    SELECT
        c.country,
        COUNT(*) AS players
    FROM rankings r
    JOIN competitors c
        ON r.competitor_id = c.competitor_id

    {where_clause}

    GROUP BY c.country
    ORDER BY players DESC
    LIMIT 10;
    """


## =====================================================
# VENUE ANALYSIS QUERIES (Dynamic Filters)
# =====================================================

def VENUES_BY_COUNTRY(where_clause="", top_n=10):
    return f"""
    SELECT
        v.country_name,
        COUNT(*) AS total_venues
    FROM venues v
    LEFT JOIN complexes cx
        ON v.complex_id = cx.complex_id

    {where_clause}

    GROUP BY v.country_name
    ORDER BY total_venues DESC
    LIMIT {top_n};
    """


def VENUES_BY_CITY(where_clause="", top_n=15):
    return f"""
    SELECT
        v.city_name,
        COUNT(*) AS total_venues
    FROM venues v
    LEFT JOIN complexes cx
        ON v.complex_id = cx.complex_id

    {where_clause}

    GROUP BY v.city_name
    ORDER BY total_venues DESC
    LIMIT {top_n};
    """


def TIMEZONE_DISTRIBUTION(where_clause="", top_n=15):
    return f"""
    SELECT
        v.timezone,
        COUNT(*) AS total_venues
    FROM venues v
    LEFT JOIN complexes cx
        ON v.complex_id = cx.complex_id

    {where_clause}

    GROUP BY v.timezone
    ORDER BY total_venues DESC
    LIMIT {top_n};
    """


def COMPLEXES_BY_COUNTRY(where_clause="", top_n=15):
    return f"""
    SELECT
        v.country_name,
        COUNT(DISTINCT cx.complex_id) AS total_complexes
    FROM venues v
    LEFT JOIN complexes cx
        ON v.complex_id = cx.complex_id

    {where_clause}

    GROUP BY v.country_name
    ORDER BY total_complexes DESC
    LIMIT {top_n};
    """


def VENUES_PER_COMPLEX(where_clause="", top_n=15):
    return f"""
    SELECT
        cx.complex_name,
        COUNT(v.venue_id) AS total_venues
    FROM complexes cx
    LEFT JOIN venues v
        ON cx.complex_id = v.complex_id

    {where_clause}

    GROUP BY cx.complex_name
    ORDER BY total_venues DESC
    LIMIT {top_n};
    """


def COUNTRY_DISTRIBUTION(where_clause="", top_n=15):
    return f"""
    SELECT
        v.country_name,
        COUNT(*) AS venues
    FROM venues v
    LEFT JOIN complexes cx
        ON v.complex_id = cx.complex_id

    {where_clause}

    GROUP BY v.country_name
    ORDER BY venues DESC
    LIMIT {top_n};
    """


def CITY_DISTRIBUTION(where_clause="", top_n=15):
    return f"""
    SELECT
        v.city_name,
        COUNT(*) AS venues
    FROM venues v
    LEFT JOIN complexes cx
        ON v.complex_id = cx.complex_id

    {where_clause}

    GROUP BY v.city_name
    ORDER BY venues DESC
    LIMIT {top_n};
    """


def TOP20_VENUES(where_clause=""):
    return f"""
    SELECT
        v.venue_name,
        v.city_name,
        v.country_name,
        v.timezone,
        cx.complex_name
    FROM venues v
    LEFT JOIN complexes cx
        ON v.complex_id = cx.complex_id

    {where_clause}

    ORDER BY v.venue_name
    LIMIT 20;
    """