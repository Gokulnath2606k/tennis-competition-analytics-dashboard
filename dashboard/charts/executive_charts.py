import plotly.express as px


# ----------------------------------------------------
# Competition by Category
# ----------------------------------------------------

def competition_category_chart(df):

    fig = px.bar(
        df,
        x="category_name",
        y="competitions",
        text="competitions",
        color="competitions",
        title="Competitions by Category"
    )

    fig.update_layout(
        template="plotly_dark",
        height=450
    )

    return fig


# ----------------------------------------------------
# Gender Distribution
# ----------------------------------------------------

def gender_chart(df):

    fig = px.pie(
        df,
        names="gender",
        values="competitions",
        hole=.55,
        title="Competition Gender Distribution"
    )

    fig.update_layout(template="plotly_dark")

    return fig


# ----------------------------------------------------
# Players by Country
# ----------------------------------------------------

def player_country_chart(df):

    fig = px.bar(
        df,
        x="players",
        y="country",
        orientation="h",
        text="players",
        color="players",
        title="Top Countries by Players"
    )

    fig.update_layout(
        template="plotly_dark",
        height=500
    )

    return fig


# ----------------------------------------------------
# Venue Countries
# ----------------------------------------------------

def venue_country_chart(df):

    fig = px.bar(
        df,
        x="country_name",
        y="venues",
        color="venues",
        text="venues",
        title="Top Venue Countries"
    )

    fig.update_layout(template="plotly_dark")

    return fig


# ----------------------------------------------------
# Ranking Distribution
# ----------------------------------------------------

def ranking_distribution(df):

    fig = px.histogram(
        df,
        x="points",
        nbins=30,
        title="Ranking Points Distribution"
    )

    fig.update_layout(template="plotly_dark")

    return fig


# ----------------------------------------------------
# Rank vs Points
# ----------------------------------------------------

def rank_scatter(df):

    fig = px.scatter(
        df,
        x="rank_position",
        y="points",
        hover_name="competitor_name",
        color="country",
        title="Rank Position vs Points"
    )

    fig.update_layout(template="plotly_dark")

    return fig  