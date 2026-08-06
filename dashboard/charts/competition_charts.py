import plotly.express as px


# =====================================================
# Common Layout
# =====================================================

def style_chart(fig):

    fig.update_layout(
        title_x=0.5,
        title_font_size=22,
        template="plotly_white",
        font=dict(size=14),
        legend_title_text=""
    )

    return fig


# =====================================================
# 1. Competitions by Category
# =====================================================

def competition_category_chart(df):

    fig = px.bar(
        df,
        x="category_name",
        y="competitions",
        color="competitions",
        text="competitions",
        title="Competitions by Category"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        xaxis_title="Category",
        yaxis_title="Competitions"
    )

    return style_chart(fig)


# =====================================================
# 2. Competition Type
# =====================================================

def competition_type_chart(df):

    fig = px.pie(
        df,
        names="type",
        values="competitions",
        hole=0.45,
        title="Competition Type Distribution"
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    return style_chart(fig)


# =====================================================
# 3. Competition Gender
# =====================================================

def competition_gender_chart(df):

    fig = px.pie(
        df,
        names="gender",
        values="competitions",
        hole=0.45,
        title="Competition Gender Distribution"
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    return style_chart(fig)


# =====================================================
# 4. Category vs Gender
# =====================================================

def category_gender_chart(df):

    fig = px.bar(
        df,
        x="category_name",
        y="total",
        color="gender",
        barmode="stack",
        text="total",
        title="Category vs Gender"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        xaxis_title="Category",
        yaxis_title="Competitions"
    )

    return style_chart(fig)


# =====================================================
# 5. Category vs Type
# =====================================================

def category_type_chart(df):

    fig = px.sunburst(
        df,
        path=["category_name", "type"],
        values="total",
        title="Competition Type by Category"
    )

    return style_chart(fig)


# =====================================================
# 6. Top 20 Competitions
# =====================================================

def top_competition_chart(df):

    fig = px.bar(
        df,
        x="competitions",
        y="competition_name",
        orientation="h",
        color="competitions",
        text="competitions",
        title="Top 20 Competitions"
    )

    fig.update_traces(textposition="outside")

    fig.update_layout(
        xaxis_title="Competitions",
        yaxis_title="Competition Name",
        yaxis=dict(categoryorder="total ascending")
    )

    return style_chart(fig)


# =====================================================
# 7. Competition Table (Optional)
# =====================================================

def competition_table(df):
    return df