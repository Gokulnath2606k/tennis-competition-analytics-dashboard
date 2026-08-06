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
# 1. Venues by Country
# =====================================================

def venue_country_chart(df):

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
# 2. Top Cities by Venues
# =====================================================

def venue_city_chart(df):

    fig = px.bar(
        df,
        x="city_name",
        y="total_venues",
        color="total_venues",
        text="total_venues",
        title="Top Cities by Venues"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        xaxis_title="City",
        yaxis_title="Number of Venues"
    )

    return style_chart(fig)


# =====================================================
# 3. Venue Timezones
# =====================================================

def timezone_chart(df):

    fig = px.bar(
        df,
        x="timezone",
        y="total_venues",
        color="total_venues",
        text="total_venues",
        title="Venue Timezones"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        xaxis_title="Timezone",
        yaxis_title="Venues"
    )

    return style_chart(fig)


# =====================================================
# 4. Complexes by Country
# =====================================================

def complexes_country_chart(df):

    fig = px.bar(
        df,
        x="country_name",
        y="total_complexes",
        color="total_complexes",
        text="total_complexes",
        title="Complexes by Country"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        xaxis_title="Country",
        yaxis_title="Complexes"
    )

    return style_chart(fig)


# =====================================================
# 5. Venues per Complex
# =====================================================

def venues_complex_chart(df):

    fig = px.bar(
        df,
        x="complex_name",
        y="total_venues",
        color="total_venues",
        text="total_venues",
        title="Venues per Complex"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        xaxis_title="Complex",
        yaxis_title="Venues"
    )

    return style_chart(fig)


# =====================================================
# 6. Venue Distribution by Country
# =====================================================

def country_distribution_chart(df):

    fig = px.pie(
        df,
        names="country_name",
        values="venues",
        hole=0.45,
        title="Venue Distribution by Country"
    )

    fig.update_traces(
        textinfo="percent+label",
        textposition="inside"
    )

    return style_chart(fig)


# =====================================================
# 7. Venue Distribution by City
# =====================================================

def city_distribution_chart(df):

    fig = px.treemap(
        df,
        path=["city_name"],
        values="venues",
        title="Venue Distribution by City"
    )

    return style_chart(fig)