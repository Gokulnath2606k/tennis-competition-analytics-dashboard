import plotly.express as px

# =====================================================
# Common Chart Style
# =====================================================

def style_chart(fig):

    fig.update_layout(
        template="plotly_white",
        title_x=0.5,
        title_font_size=22,
        font=dict(size=14),
        legend_title_text=""
    )

    return fig


# =====================================================
# 1. Top Players by Ranking Points
# =====================================================

def top_players_points_chart(df):

    fig = px.bar(
        df,
        x="competitor_name",
        y="points",
        color="points",
        text="points",
        title="Top Players by Ranking Points"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        xaxis_title="Player",
        yaxis_title="Ranking Points"
    )

    return style_chart(fig)


# =====================================================
# 2. Competitions Played
# =====================================================

def competitions_played_chart(df):

    fig = px.bar(
        df,
        x="competitor_name",
        y="competitions_played",
        color="competitions_played",
        text="competitions_played",
        title="Top Players by Competitions Played"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        xaxis_title="Player",
        yaxis_title="Competitions Played"
    )

    return style_chart(fig)


# =====================================================
# 3. Ranking Movement
# =====================================================

def ranking_movement_chart(df):

    fig = px.bar(
        df,
        x="movement",
        y="players",
        color="players",
        text="players",
        title="Ranking Movement Distribution"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        xaxis_title="Movement",
        yaxis_title="Number of Players"
    )

    return style_chart(fig)


# =====================================================
# 4. Ranking Points by Country
# =====================================================

def country_points_chart(df):

    fig = px.bar(
        df,
        x="country",
        y="total_points",
        color="total_points",
        text="total_points",
        title="Ranking Points by Country"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        xaxis_title="Country",
        yaxis_title="Total Ranking Points"
    )

    return style_chart(fig)


# =====================================================
# 5. Average Points by Country
# =====================================================

def average_points_chart(df):

    fig = px.bar(
        df,
        x="country",
        y="avg_points",
        color="avg_points",
        text="avg_points",
        title="Average Ranking Points by Country"
    )

    fig.update_traces(texttemplate="%{text:.0f}")

    fig.update_layout(
        xaxis_title="Country",
        yaxis_title="Average Points"
    )

    return style_chart(fig)


# =====================================================
# 6. Top Ranked Players by Country
# =====================================================

def top_countries_chart(df):

    fig = px.pie(
        df,
        names="country",
        values="players",
        hole=0.45,
        title="Top Ranked Players by Country"
    )

    fig.update_traces(
        textinfo="percent+label",
        textposition="inside"
    )

    return style_chart(fig)


# =====================================================
# 7. Player Distribution
# =====================================================

def player_distribution_chart(df):

    fig = px.treemap(
        df,
        path=["country"],
        values="players",
        title="Player Distribution by Country"
    )

    return style_chart(fig)