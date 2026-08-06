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
# 1. Players by Country
# =====================================================

def players_country_chart(df):

    fig = px.bar(
        df,
        x="country",
        y="total_players",
        color="total_players",
        text="total_players",
        title="Players by Country"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        xaxis_title="Country",
        yaxis_title="Number of Players"
    )

    return style_chart(fig)


# =====================================================
# 2. Venues by Country
# =====================================================

def venues_country_chart(df):

    fig = px.bar(
        df,
        x="country_name",
        y="total_venues",
        color="total_venues",
        text="total_venues",
        title="Venues by Country"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        xaxis_title="Country",
        yaxis_title="Number of Venues"
    )

    return style_chart(fig)


# =====================================================
# 3. Ranking Points by Country
# =====================================================

def points_country_chart(df):

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
# 4. Average Ranking Points
# =====================================================

def average_points_chart(df):

    fig = px.bar(
        df,
        x="country",
        y="avg_points",
        color="avg_points",
        text="avg_points",
        title="Average Ranking Points"
    )

    fig.update_traces(texttemplate="%{text:.0f}")

    fig.update_layout(
        xaxis_title="Country",
        yaxis_title="Average Points"
    )

    return style_chart(fig)


# =====================================================
# 5. Top Players by Country
# =====================================================

def top_players_chart(df):

    fig = px.pie(
        df,
        names="country",
        values="top_players",
        hole=0.45,
        title="Top Players by Country"
    )

    fig.update_traces(
        textinfo="percent+label",
        textposition="inside"
    )

    return style_chart(fig)


# =====================================================
# 6. Player Distribution
# =====================================================

def player_distribution_chart(df):

    fig = px.treemap(
        df,
        path=["country"],
        values="players",
        title="Player Distribution Across Countries"
    )

    return style_chart(fig)


# =====================================================
# 7. Top Countries by Ranking Points
# =====================================================

def top_country_points_chart(df):

    fig = px.bar(
        df,
        x="country",
        y="total_points",
        color="total_points",
        text="total_points",
        title="Top Countries by Ranking Points"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        xaxis_title="Country",
        yaxis_title="Ranking Points"
    )

    return style_chart(fig)