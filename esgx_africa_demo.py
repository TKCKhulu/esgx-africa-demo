"""
ESGx.Africa - Comprehensive Platform Demo
AI-Powered ESG Intelligence for Africa with Ubuntu Philosophy
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import json

# Page configuration
st.set_page_config(
    page_title="ESGx.Africa - Ubuntu ESG Platform",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1c7e57;
        text-align: center;
        margin-bottom: 1rem;
    }
    .ubuntu-card {
        background: linear-gradient(135deg, #1c7e57, #28a85c);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #1c7e57;
        margin: 0.5rem 0;
    }
    .subscription-card {
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem;
        text-align: center;
    }
    .featured-card {
        border: 3px solid #1c7e57;
        background: #f0f8f5;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">🌍 ESGx.Africa</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">AI-Powered ESG Intelligence for Africa | Ubuntu Philosophy Integrated</p>', unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.image("https://via.placeholder.com/200x80/1c7e57/ffffff?text=ESGx.Africa", width=200)
page = st.sidebar.selectbox(
    "Navigate to:",
    ["🏠 Home Dashboard", "📊 Ubuntu ESG Calculator", "🤖 AI ESG Agents", "📈 Analytics & Reports", 
     "🏢 Organization Profile", "💰 Subscription Plans", "🎓 ESGx Academy", "🌱 Carbon Accounting"]
)

# Sample data for demonstration
sample_org_data = {
    "name": "Ubuntu Mining Corp",
    "country": "South Africa",
    "industry": "Mining",
    "employees": 2500,
    "subscription": "Growth Pro"
}

# Home Dashboard
if page == "🏠 Home Dashboard":
    
    # Welcome message
    st.markdown("""
    <div class="ubuntu-card">
        <h2>Welcome to ESGx.Africa</h2>
        <p>Africa's first AI-powered ESG platform integrating Ubuntu philosophy with international standards.</p>
        <p><strong>Ubuntu:</strong> "I am because we are" - Community-centered sustainability for Africa's future.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Overall ESG Score",
            value="78.2",
            delta="↑ 5.3 vs last quarter",
            help="African-contextualized ESG score with Ubuntu integration"
        )
    
    with col2:
        st.metric(
            label="Ubuntu Index™",
            value="82.5",
            delta="↑ 8.1 vs last quarter", 
            help="Ubuntu philosophy integration score"
        )
    
    with col3:
        st.metric(
            label="BEE Compliance",
            value="Level 4",
            delta="Improved from Level 6",
            help="Broad-Based Black Economic Empowerment level"
        )
    
    with col4:
        st.metric(
            label="Carbon Intensity",
            value="4.2 tCO₂e",
            delta="↓ 12% reduction",
            help="Carbon emissions per employee"
        )
    
    # ESG Performance Chart
    st.subheader("📈 ESG Performance Overview")
    
    # Create sample data for demonstration
    categories = ['Environmental', 'Social', 'Governance', 'Ubuntu Index']
    current_scores = [72, 85, 76, 82.5]
    previous_scores = [68, 78, 74, 76]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Current Quarter',
        x=categories,
        y=current_scores,
        marker_color='#1c7e57'
    ))
    fig.add_trace(go.Bar(
        name='Previous Quarter',
        x=categories,
        y=previous_scores,
        marker_color='#a8d8b9'
    ))
    
    fig.update_layout(
        title='ESG Performance by Component',
        yaxis_title='Score (0-100)',
        barmode='group',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Recent Activities
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Recent ESG Activities")
        activities = [
            {"date": "2024-01-15", "activity": "Community water project completed", "impact": "500 families benefited"},
            {"date": "2024-01-12", "activity": "Local supplier training program", "impact": "25 SMEs trained"},
            {"date": "2024-01-10", "activity": "Solar panel installation", "impact": "30% renewable energy"},
            {"date": "2024-01-08", "activity": "BEE certification renewal", "impact": "Level 4 achieved"}
        ]
        
        for activity in activities:
            st.markdown(f"""
            <div class="metric-card">
                <strong>{activity['date']}</strong><br>
                {activity['activity']}<br>
                <small style="color: #1c7e57;">{activity['impact']}</small>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.subheader("⚠️ Action Items")
        action_items = [
            {"priority": "High", "item": "Update water usage reporting", "due": "Jan 20"},
            {"priority": "Medium", "item": "Schedule community consultation", "due": "Jan 25"},
            {"priority": "Low", "item": "Review governance policies", "due": "Feb 15"},
            {"priority": "Medium", "item": "Submit quarterly ESG report", "due": "Jan 30"}
        ]
        
        for item in action_items:
            color = "#dc3545" if item["priority"] == "High" else "#ffc107" if item["priority"] == "Medium" else "#28a745"
            st.markdown(f"""
            <div class="metric-card" style="border-left-color: {color};">
                <strong style="color: {color};">{item['priority']} Priority</strong><br>
                {item['item']}<br>
                <small>Due: {item['due']}</small>
            </div>
            """, unsafe_allow_html=True)

# Ubuntu ESG Calculator
elif page == "📊 Ubuntu ESG Calculator":
    
    st.header("Ubuntu ESG Calculator")
    st.markdown("Calculate your organization's ESG score with Ubuntu philosophy integration")
    
    # Input form
    with st.form("esg_calculator"):
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🌍 Environmental Metrics")
            carbon_emissions = st.slider("Carbon Emissions Reduction (%)", 0, 100, 35)
            renewable_energy = st.slider("Renewable Energy Usage (%)", 0, 100, 25)
            water_efficiency = st.slider("Water Efficiency Score", 0, 100, 60)
            waste_reduction = st.slider("Waste Reduction (%)", 0, 100, 40)
            
            st.subheader("🏛️ Governance Metrics")
            board_diversity = st.slider("Board Diversity Score", 0, 100, 65)
            transparency = st.slider("Transparency & Disclosure", 0, 100, 75)
            ethics_score = st.slider("Ethics & Anti-corruption", 0, 100, 80)
        
        with col2:
            st.subheader("👥 Social Metrics")
            employee_wellbeing = st.slider("Employee Wellbeing", 0, 100, 70)
            community_engagement = st.slider("Community Engagement", 0, 100, 85)
            diversity_inclusion = st.slider("Diversity & Inclusion", 0, 100, 68)
            local_employment = st.slider("Local Employment (%)", 0, 100, 75)
            
            st.subheader("🤝 Ubuntu Index Components")
            local_procurement = st.slider("Local Procurement (%)", 0, 100, 45)
            cultural_preservation = st.slider("Cultural Preservation", 0, 100, 60)
            indigenous_knowledge = st.slider("Indigenous Knowledge Integration", 0, 100, 55)
            community_investment = st.slider("Community Investment (% of revenue)", 0, 10, 2)
        
        submitted = st.form_submit_button("🧮 Calculate Ubuntu ESG Score", type="primary")
    
    if submitted:
        # Calculate scores (simplified algorithm)
        env_score = (carbon_emissions * 0.3 + renewable_energy * 0.25 + 
                    water_efficiency * 0.25 + waste_reduction * 0.2)
        
        social_score = (employee_wellbeing * 0.25 + community_engagement * 0.25 + 
                       diversity_inclusion * 0.25 + local_employment * 0.25)
        
        governance_score = (board_diversity * 0.35 + transparency * 0.35 + ethics_score * 0.3)
        
        ubuntu_score = (local_procurement * 0.25 + cultural_preservation * 0.2 + 
                       indigenous_knowledge * 0.2 + (community_investment * 10) * 0.2 + 
                       community_engagement * 0.15)
        
        # Overall ESG score with Ubuntu integration
        overall_score = (env_score * 0.25 + social_score * 0.35 + 
                        governance_score * 0.25 + ubuntu_score * 0.15)
        
        # Display results
        st.success("✅ Ubuntu ESG Score Calculated Successfully!")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Overall ESG Score", f"{overall_score:.1f}/100")
            st.metric("Environmental", f"{env_score:.1f}/100")
            st.metric("Social", f"{social_score:.1f}/100")
        
        with col2:
            st.metric("Governance", f"{governance_score:.1f}/100")
            st.metric("Ubuntu Index™", f"{ubuntu_score:.1f}/100")
            
            # ESG Rating
            if overall_score >= 80:
                rating = "AA"
                color = "green"
            elif overall_score >= 70:
                rating = "A"
                color = "lightgreen"
            elif overall_score >= 60:
                rating = "BBB"
                color = "orange"
            else:
                rating = "BB"
                color = "red"
            
            st.markdown(f"<h3 style='color: {color};'>ESG Rating: {rating}</h3>", unsafe_allow_html=True)
        
        with col3:
            # Ubuntu Rating
            if ubuntu_score >= 80:
                ubuntu_rating = "Ubuntu Champion"
            elif ubuntu_score >= 65:
                ubuntu_rating = "Ubuntu Advocate"
            elif ubuntu_score >= 50:
                ubuntu_rating = "Ubuntu Aligned"
            else:
                ubuntu_rating = "Ubuntu Developing"
            
            st.markdown(f"<h3 style='color: #1c7e57;'>{ubuntu_rating}</h3>", unsafe_allow_html=True)
        
        # Radar chart
        fig = go.Figure()
        
        categories = ['Environmental', 'Social', 'Governance', 'Ubuntu Index']
        values = [env_score, social_score, governance_score, ubuntu_score]
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Current Scores',
            line_color='#1c7e57'
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )),
            showlegend=True,
            title="ESG Performance Radar Chart"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # AI Insights
        st.subheader("🤖 AI-Generated Insights")
        
        insights = []
        if ubuntu_score > 75:
            insights.append("✅ Strong Ubuntu philosophy integration - excellent community focus")
        if env_score < 60:
            insights.append("⚠️ Environmental performance needs improvement - consider renewable energy investments")
        if social_score > 80:
            insights.append("✅ Excellent social performance - strong employee and community relations")
        if governance_score < 65:
            insights.append("⚠️ Governance could be strengthened - review board composition and transparency")
        
        for insight in insights:
            st.markdown(f"- {insight}")

# AI ESG Agents
elif page == "🤖 AI ESG Agents":
    
    st.header("AI ESG Agents - Ubuntu GPT Powered")
    st.markdown("Interact with our specialized AI agents for ESG guidance and insights")
    
    # Agent selection
    agent_type = st.selectbox(
        "Choose your AI Agent:",
        ["Ubuntu ESG Advisor", "Compliance Assistant", "Carbon Calculator", 
         "BEE Analyzer", "Risk Assessor", "Report Generator"]
    )
    
    # Agent descriptions
    agent_descriptions = {
        "Ubuntu ESG Advisor": "General ESG guidance with Ubuntu philosophy integration",
        "Compliance Assistant": "Help with African regulatory compliance and frameworks",
        "Carbon Calculator": "Carbon footprint analysis and reduction strategies",
        "BEE Analyzer": "Broad-Based Black Economic Empowerment analysis",
        "Risk Assessor": "ESG risk identification and mitigation",
        "Report Generator": "Automated ESG report creation and insights"
    }
    
    st.info(f"**{agent_type}**: {agent_descriptions[agent_type]}")
    
    # Chat interface
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input(f"Ask the {agent_type} anything about ESG..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate AI response (simulation)
        with st.chat_message("assistant"):
            if "ubuntu" in prompt.lower() or "community" in prompt.lower():
                response = """Ubuntu philosophy emphasizes interconnectedness and community wellbeing. In ESG context, this means:
                
                🤝 **Community Engagement**: Regular consultations and inclusive decision-making
                💼 **Local Procurement**: Supporting local suppliers and businesses
                🎓 **Skills Development**: Training and empowering local communities
                🌱 **Sustainable Practices**: Environmental stewardship for future generations
                
                Would you like me to help you develop a specific Ubuntu-centered initiative?"""
            
            elif "bee" in prompt.lower():
                response = """For BEE compliance in South Africa, focus on these key elements:
                
                📊 **Ownership**: Black ownership stakes in your organization
                👥 **Management Control**: Black representation in leadership
                🎯 **Skills Development**: Training programs for black employees
                🏢 **Enterprise Development**: Supporting black-owned suppliers
                💰 **Socio-Economic Development**: Community investment programs
                
                Current BEE trends favor companies with strong community impact. Need help with a specific BEE element?"""
            
            else:
                response = f"""As your {agent_type}, I'm here to help with African-contextualized ESG guidance. 
                
                Some areas I can assist with:
                - Ubuntu philosophy integration in ESG practices
                - African regulatory compliance (BEE, JSE, local laws)
                - Community-centered sustainability approaches
                - Local procurement and employment strategies
                - Cultural sensitivity in ESG implementation
                
                What specific ESG challenge would you like to discuss?"""
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# Subscription Plans
elif page == "💰 Subscription Plans":
    
    st.header("ESGx.Africa Subscription Plans")
    st.markdown("Choose the plan that fits your organization's ESG needs")
    
    # Plans data
    plans = {
        "Community Free": {
            "price_monthly": "R0",
            "price_annual": "R0", 
            "features": ["Ubuntu Index™", "SMS input", "3 reports/month", "Basic ESG scoring"],
            "max_reports": 3,
            "ai_agents": 0,
            "color": "#6c757d"
        },
        "Ubuntu Starter": {
            "price_monthly": "R2,500",
            "price_annual": "R25,000",
            "features": ["Core ESG KPIs", "ESG wizard", "Email support", "1 AI agent", "50 reports/month"],
            "max_reports": 50,
            "ai_agents": 1,
            "color": "#17a2b8"
        },
        "Growth Pro": {
            "price_monthly": "R15,000", 
            "price_annual": "R150,000",
            "features": ["2 AI agents", "JSE compliance", "ESGx metrics", "500 reports/month", "Priority support"],
            "max_reports": 500,
            "ai_agents": 2,
            "color": "#1c7e57",
            "featured": True
        },
        "Enterprise ESG": {
            "price_monthly": "R75,000",
            "price_annual": "R750,000", 
            "features": ["All AI agents", "API access", "Custom reporting", "Unlimited reports", "Dedicated support"],
            "max_reports": "Unlimited",
            "ai_agents": 5,
            "color": "#dc3545"
        },
        "Enterprise+": {
            "price_monthly": "Custom",
            "price_annual": "Avg R1.5M",
            "features": ["On-premise deployment", "White-labeling", "Dedicated AI", "Custom integrations"],
            "max_reports": "Unlimited", 
            "ai_agents": "Unlimited",
            "color": "#6f42c1"
        }
    }
    
    cols = st.columns(len(plans))
    
    for i, (plan_name, plan_data) in enumerate(plans.items()):
        with cols[i]:
            card_class = "subscription-card featured-card" if plan_data.get("featured") else "subscription-card"
            
            st.markdown(f"""
            <div class="{card_class}">
                <h3 style="color: {plan_data['color']};">{plan_name}</h3>
                <div style="font-size: 1.5rem; font-weight: bold;">
                    {plan_data['price_monthly']}/month
                </div>
                <div style="color: #666; margin-bottom: 1rem;">
                    {plan_data['price_annual']}/year
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("**Features:**")
            for feature in plan_data['features']:
                st.markdown(f"✅ {feature}")
            
            st.markdown(f"📊 **Reports/month:** {plan_data['max_reports']}")
            st.markdown(f"🤖 **AI Agents:** {plan_data['ai_agents']}")
            
            if plan_data.get("featured"):
                st.success("🌟 Most Popular")
            
            st.button(f"Choose {plan_name}", key=f"btn_{i}")
    
    # ROI Calculator
    st.subheader("📈 ROI Calculator")
    col1, col2 = st.columns(2)
    
    with col1:
        company_size = st.selectbox("Company Size", ["Small (< 50 employees)", "Medium (50-500)", "Large (500+)"])
        industry = st.selectbox("Industry", ["Mining", "Agriculture", "Manufacturing", "Financial Services", "Energy", "Other"])
        current_esg_spend = st.number_input("Current annual ESG spending (R)", value=500000)
    
    with col2:
        # Calculate estimated ROI
        base_savings = current_esg_spend * 0.15  # 15% efficiency savings
        compliance_benefits = 200000  # Estimated compliance cost avoidance
        investment_attraction = 1000000  # Estimated additional investment
        
        total_benefits = base_savings + compliance_benefits + investment_attraction
        
        st.metric("Estimated Annual Benefits", f"R{total_benefits:,.0f}")
        st.metric("ESG Efficiency Savings", f"R{base_savings:,.0f}")
        st.metric("Compliance Cost Avoidance", f"R{compliance_benefits:,.0f}")
        st.metric("Additional Investment Attraction", f"R{investment_attraction:,.0f}")

# Analytics & Reports
elif page == "📈 Analytics & Reports":
    
    st.header("ESG Analytics & Reports")
    
    # Time period selector
    col1, col2 = st.columns([1, 3])
    with col1:
        time_period = st.selectbox("Time Period", ["Last 12 months", "Last 6 months", "Last quarter", "Custom"])
    
    # Key trends
    st.subheader("📊 ESG Trends Over Time")
    
    # Generate sample time series data
    dates = pd.date_range(start='2023-01-01', end='2024-01-01', freq='M')
    np.random.seed(42)
    
    df = pd.DataFrame({
        'Date': dates,
        'Overall ESG': 60 + np.cumsum(np.random.normal(1, 2, len(dates))),
        'Environmental': 55 + np.cumsum(np.random.normal(1.2, 2.5, len(dates))),
        'Social': 65 + np.cumsum(np.random.normal(0.8, 1.8, len(dates))),
        'Governance': 58 + np.cumsum(np.random.normal(1.1, 2.2, len(dates))),
        'Ubuntu Index': 45 + np.cumsum(np.random.normal(2, 2.5, len(dates)))
    })
    
    fig = px.line(df, x='Date', y=['Overall ESG', 'Environmental', 'Social', 'Governance', 'Ubuntu Index'],
                  title='ESG Performance Trends')
    fig.update_layout(height=400, yaxis_title='Score (0-100)')
    st.plotly_chart(fig, use_container_width=True)
    
    # Industry benchmarking
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏭 Industry Benchmarking")
        
        benchmark_data = {
            'Your Company': [78, 82, 76, 83],
            'Industry Average': [65, 70, 68, 60],
            'Top Quartile': [85, 88, 84, 80]
        }
        
        categories = ['Environmental', 'Social', 'Governance', 'Ubuntu']
        
        fig = go.Figure()
        for company, scores in benchmark_data.items():
            fig.add_trace(go.Scatterpolar(
                r=scores,
                theta=categories,
                fill='toself' if company == 'Your Company' else None,
                name=company
            ))
        
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=True,
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🎯 Goal Progress")
        
        goals = [
            {"goal": "Net Zero by 2030", "progress": 65, "target": 100},
            {"goal": "50% Local Procurement", "progress": 42, "target": 50},
            {"goal": "BEE Level 3", "progress": 75, "target": 100},
            {"goal": "Zero Workplace Incidents", "progress": 88, "target": 100}
        ]
        
        for goal in goals:
            progress_pct = (goal["progress"] / goal["target"]) * 100
            st.markdown(f"**{goal['goal']}**")
            st.progress(progress_pct / 100)
            st.markdown(f"{progress_pct:.0f}% complete")
            st.markdown("---")

# Organization Profile
elif page == "🏢 Organization Profile":
    
    st.header("Organization Profile")
    
    # Organization details
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Company Information")
        
        # Editable form
        with st.form("org_profile"):
            org_name = st.text_input("Organization Name", value=sample_org_data["name"])
            country = st.selectbox("Country", ["South Africa", "Kenya", "Nigeria", "Ghana", "Other"], 
                                 index=0 if sample_org_data["country"] == "South Africa" else 4)
            industry = st.selectbox("Industry", ["Mining", "Agriculture", "Manufacturing", "Financial Services"], 
                                  index=0 if sample_org_data["industry"] == "Mining" else 0)
            employees = st.number_input("Number of Employees", value=sample_org_data["employees"])
            
            col_form1, col_form2 = st.columns(2)
            with col_form1:
                bee_level = st.selectbox("BEE Level", ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Level 6", "Level 7", "Level 8"])
                jse_listed = st.checkbox("JSE Listed")
            
            with col_form2:
                sustainability_officer = st.text_input("Sustainability Officer", value="Jane Doe")
                esg_policy_url = st.text_input("ESG Policy URL")
            
            submitted = st.form_submit_button("Update Profile")
            
            if submitted:
                st.success("✅ Profile updated successfully!")
    
    with col2:
        st.subheader("Quick Stats")
        
        st.metric("Current ESG Rating", "A-", help="Based on latest assessment")
        st.metric("Ubuntu Index™", "82.5", "↑ 8.1", help="Ubuntu philosophy integration")
        st.metric("Reports Generated", "47", help="This month")
        st.metric("Compliance Status", "✅ Good", help="All requirements met")
        
        # Ubuntu initiatives
        st.subheader("🤝 Ubuntu Initiatives")
        ubuntu_initiatives = [
            "Community water project",
            "Local supplier development",
            "Cultural heritage preservation",
            "Skills development program"
        ]
        
        for initiative in ubuntu_initiatives:
            st.markdown(f"✅ {initiative}")

# ESGx Academy
elif page == "🎓 ESGx Academy":
    
    st.header("ESGx Academy")
    st.markdown("Learn ESG best practices with African context and Ubuntu philosophy")
    
    # Course categories
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("📚 Fundamentals")
        courses = [
            "ESG Basics for Africa",
            "Ubuntu Philosophy in Business",
            "BEE Compliance 101",
            "JSE Sustainability Reporting"
        ]
        
        for course in courses:
            if st.button(course, key=f"fund_{course}"):
                st.info(f"Starting course: {course}")
    
    with col2:
        st.subheader("🌍 Environmental")
        courses = [
            "Carbon Accounting for Africa",
            "Water Management in Arid Regions",
            "Renewable Energy Transitions",
            "Biodiversity Conservation"
        ]
        
        for course in courses:
            if st.button(course, key=f"env_{course}"):
                st.info(f"Starting course: {course}")
    
    with col3:
        st.subheader("👥 Social & Governance")
        courses = [
            "Community Engagement Strategies",
            "Inclusive Governance Models",
            "Indigenous Rights & ESG",
            "Stakeholder Capitalism"
        ]
        
        for course in courses:
            if st.button(course, key=f"soc_{course}"):
                st.info(f"Starting course: {course}")
    
    # Featured course
    st.subheader("🌟 Featured Course: Ubuntu ESG Leadership")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Learn how to integrate Ubuntu philosophy into modern ESG practices**
        
        📖 **What you'll learn:**
        - Ubuntu philosophy fundamentals
        - Community-centered sustainability
        - African ESG frameworks integration
        - Cultural sensitivity in ESG implementation
        - Local stakeholder engagement
        
        ⏱️ **Duration:** 4 weeks  
        🎓 **Certificate:** ESGx Academy Ubuntu ESG Leadership  
        👥 **Level:** Intermediate  
        """)
    
    with col2:
        st.info("💰 **Price:** R2,500")
        st.success("⭐ 4.8/5 rating (127 reviews)")
        
        if st.button("🚀 Enroll Now", type="primary"):
            st.balloons()
            st.success("🎉 Enrolled successfully! Welcome to Ubuntu ESG Leadership.")

# Carbon Accounting
elif page == "🌱 Carbon Accounting":
    
    st.header("Carbon Accounting & Offset Management")
    st.markdown("Track, reduce, and offset your carbon emissions with African carbon markets")
    
    # Carbon dashboard
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Emissions", "12,450 tCO₂e", "↓ 8% vs last year")
    
    with col2:
        st.metric("Scope 1", "4,200 tCO₂e", "↓ 12%")
    
    with col3:
        st.metric("Scope 2", "6,800 tCO₂e", "↓ 5%")
    
    with col4:
        st.metric("Scope 3", "1,450 tCO₂e", "↑ 3%")
    
    # Emissions breakdown chart
    st.subheader("📊 Emissions Breakdown")
    
    # Sample data for emissions by source
    emissions_data = {
        'Source': ['Electricity', 'Vehicles', 'Manufacturing', 'Business Travel', 'Waste', 'Other'],
        'Emissions': [6800, 2500, 1700, 800, 450, 200],
        'Scope': ['Scope 2', 'Scope 1', 'Scope 1', 'Scope 3', 'Scope 3', 'Scope 1']
    }
    
    df_emissions = pd.DataFrame(emissions_data)
    
    fig = px.pie(df_emissions, values='Emissions', names='Source', 
                 title='Emissions by Source', color='Scope',
                 color_discrete_map={'Scope 1': '#ff7f0e', 'Scope 2': '#2ca02c', 'Scope 3': '#1f77b4'})
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Carbon offset opportunities
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🌳 African Carbon Offset Projects")
        
        offset_projects = [
            {
                "name": "Kenyan Reforestation Initiative",
                "type": "Forestry",
                "price": "R85/tCO₂e",
                "location": "Kenya",
                "certification": "Verified Carbon Standard",
                "co_benefits": "Biodiversity, Community employment"
            },
            {
                "name": "South African Solar Cookstoves",
                "type": "Clean Technology",
                "price": "R125/tCO₂e", 
                "location": "South Africa",
                "certification": "Gold Standard",
                "co_benefits": "Health, Women empowerment"
            },
            {
                "name": "Nigerian Waste-to-Energy",
                "type": "Waste Management",
                "price": "R110/tCO₂e",
                "location": "Nigeria", 
                "certification": "Clean Development Mechanism",
                "co_benefits": "Waste reduction, Energy access"
            }
        ]
        
        for project in offset_projects:
            with st.expander(f"{project['name']} - {project['price']}"):
                st.markdown(f"**Type:** {project['type']}")
                st.markdown(f"**Location:** {project['location']}")
                st.markdown(f"**Certification:** {project['certification']}")
                st.markdown(f"**Co-benefits:** {project['co_benefits']}")
                
                tonnes = st.number_input(f"Tonnes to offset", min_value=0, max_value=1000, value=100, key=project['name'])
                cost = tonnes * int(project['price'].replace('R', '').replace('/tCO₂e', ''))
                st.markdown(f"**Total Cost:** R{cost:,}")
                
                if st.button(f"Purchase Offsets", key=f"purchase_{project['name']}"):
                    st.success(f"✅ Purchased {tonnes} tCO₂e offsets from {project['name']}")
    
    with col2:
        st.subheader("🎯 Net Zero Pathway")
        
        # Net zero trajectory
        years = list(range(2024, 2031))
        current_emissions = 12450
        
        # Simulated reduction pathway
        emissions_trajectory = []
        for year in years:
            reduction = (year - 2024) * 0.08  # 8% annual reduction
            emissions = current_emissions * (1 - reduction)
            emissions_trajectory.append(max(emissions, 0))
        
        df_trajectory = pd.DataFrame({
            'Year': years,
            'Emissions': emissions_trajectory,
            'Target': [current_emissions * (1 - 0.1 * (year - 2024)) for year in years]
        })
        
        fig = px.line(df_trajectory, x='Year', y=['Emissions', 'Target'],
                     title='Net Zero Trajectory',
                     labels={'value': 'Emissions (tCO₂e)', 'variable': 'Type'})
        
        fig.add_hline(y=0, line_dash="dash", line_color="green", 
                     annotation_text="Net Zero Target")
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Reduction strategies
        st.subheader("💡 Reduction Strategies")
        
        strategies = [
            {"strategy": "Solar panel installation", "potential": "2,500 tCO₂e/year", "cost": "R2.5M", "payback": "3 years"},
            {"strategy": "Fleet electrification", "potential": "1,800 tCO₂e/year", "cost": "R5M", "payback": "5 years"},
            {"strategy": "Energy efficiency upgrades", "potential": "1,200 tCO₂e/year", "cost": "R1.2M", "payback": "2 years"},
            {"strategy": "Waste reduction program", "potential": "400 tCO₂e/year", "cost": "R200k", "payback": "1 year"}
        ]
        
        for strategy in strategies:
            with st.expander(strategy["strategy"]):
                col_s1, col_s2 = st.columns(2)
                with col_s1:
                    st.markdown(f"**Reduction potential:** {strategy['potential']}")
                    st.markdown(f"**Investment required:** {strategy['cost']}")
                with col_s2:
                    st.markdown(f"**Payback period:** {strategy['payback']}")
                    if st.button("Add to Plan", key=f"strategy_{strategy['strategy']}"):
                        st.info("Added to carbon reduction plan")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        <p>ESGx.Africa™ | Powered by Ubuntu Philosophy | Made for Africa 🌍</p>
        <p>Transforming sustainability compliance through African-built, AI-driven ESG infrastructure</p>
    </div>
    """, 
    unsafe_allow_html=True
)