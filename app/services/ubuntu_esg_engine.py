"""
ESGx.Africa Ubuntu ESG Engine
Core service for calculating ESG scores with Ubuntu philosophy integration
"""

import json
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
import logging
import asyncio

from sqlalchemy.orm import Session
from app.models.esg_score import ESGScore
from app.models.organization import Organization
from app.models.carbon_data import CarbonData
from app.models.compliance import ComplianceRecord
from app.core.config import settings

logger = logging.getLogger(__name__)

class UbuntuESGEngine:
    """
    Core engine for calculating ESG scores with Ubuntu philosophy integration
    Implements African-contextualized ESG assessment methodology
    """
    
    def __init__(self):
        self.ubuntu_weights = {
            "community_engagement": 0.25,
            "local_procurement": 0.20,
            "cultural_preservation": 0.15,
            "indigenous_knowledge": 0.15,
            "local_employment": 0.15,
            "community_investment": 0.10
        }
        
        self.esg_weights = {
            "environmental": 0.25,
            "social": 0.35,  # Higher weight in African context
            "governance": 0.25,
            "ubuntu": 0.15   # Ubuntu philosophy component
        }
    
    def calculate_ubuntu_index(
        self, 
        organization_data: Dict[str, Any],
        community_data: Dict[str, Any] = None
    ) -> Tuple[float, Dict[str, Any]]:
        """
        Calculate Ubuntu Index™ - African philosophy integration score
        
        Args:
            organization_data: Organization information and activities
            community_data: Community engagement and impact data
            
        Returns:
            Tuple of (ubuntu_score, detailed_breakdown)
        """
        
        ubuntu_components = {}
        total_score = 0.0
        
        # Community Engagement Score (25%)
        community_score = self._calculate_community_engagement(
            organization_data.get("community_activities", {}),
            community_data or {}
        )
        ubuntu_components["community_engagement"] = community_score
        total_score += community_score * self.ubuntu_weights["community_engagement"]
        
        # Local Procurement Score (20%)
        procurement_score = self._calculate_local_procurement(
            organization_data.get("procurement_data", {})
        )
        ubuntu_components["local_procurement"] = procurement_score
        total_score += procurement_score * self.ubuntu_weights["local_procurement"]
        
        # Cultural Preservation Score (15%)
        cultural_score = self._calculate_cultural_preservation(
            organization_data.get("cultural_initiatives", {})
        )
        ubuntu_components["cultural_preservation"] = cultural_score
        total_score += cultural_score * self.ubuntu_weights["cultural_preservation"]
        
        # Indigenous Knowledge Score (15%)
        indigenous_score = self._calculate_indigenous_knowledge_integration(
            organization_data.get("indigenous_practices", {})
        )
        ubuntu_components["indigenous_knowledge"] = indigenous_score
        total_score += indigenous_score * self.ubuntu_weights["indigenous_knowledge"]
        
        # Local Employment Score (15%)
        employment_score = self._calculate_local_employment(
            organization_data.get("employment_data", {})
        )
        ubuntu_components["local_employment"] = employment_score
        total_score += employment_score * self.ubuntu_weights["local_employment"]
        
        # Community Investment Score (10%)
        investment_score = self._calculate_community_investment(
            organization_data.get("community_investment", {})
        )
        ubuntu_components["community_investment"] = investment_score
        total_score += investment_score * self.ubuntu_weights["community_investment"]
        
        return round(total_score, 2), ubuntu_components
    
    def calculate_comprehensive_esg_score(
        self,
        organization: Organization,
        environmental_data: Dict[str, Any],
        social_data: Dict[str, Any],
        governance_data: Dict[str, Any],
        ubuntu_data: Dict[str, Any],
        db: Session
    ) -> ESGScore:
        """
        Calculate comprehensive ESG score with Ubuntu integration
        
        Args:
            organization: Organization instance
            environmental_data: Environmental performance data
            social_data: Social performance data
            governance_data: Governance performance data
            ubuntu_data: Ubuntu philosophy data
            db: Database session
            
        Returns:
            ESGScore instance with calculated scores
        """
        
        # Calculate individual component scores
        env_score = self._calculate_environmental_score(environmental_data, organization)
        social_score = self._calculate_social_score(social_data, organization)
        governance_score = self._calculate_governance_score(governance_data, organization)
        
        # Calculate Ubuntu Index
        ubuntu_score, ubuntu_components = self.calculate_ubuntu_index(
            ubuntu_data,
            social_data.get("community_data", {})
        )
        
        # Calculate weighted overall ESG score
        overall_score = (
            env_score * self.esg_weights["environmental"] +
            social_score * self.esg_weights["social"] +
            governance_score * self.esg_weights["governance"] +
            ubuntu_score * self.esg_weights["ubuntu"]
        )
        
        # Get African-specific metrics
        bee_score = self._calculate_bee_compliance_score(organization, db)
        local_employment_score = self._calculate_local_employment_score(social_data)
        community_investment_score = self._calculate_community_investment_score(ubuntu_data)
        
        # Create ESGScore instance
        esg_score = ESGScore(
            organization_id=organization.id,
            environmental_score=round(env_score, 2),
            social_score=round(social_score, 2),
            governance_score=round(governance_score, 2),
            overall_esg_score=round(overall_score, 2),
            ubuntu_index=round(ubuntu_score, 2),
            bee_compliance_score=round(bee_score, 2),
            local_employment_score=round(local_employment_score, 2),
            community_investment_score=round(community_investment_score, 2),
            ubuntu_components=ubuntu_components,
            environmental_components=environmental_data,
            social_components=social_data,
            governance_components=governance_data,
            reporting_period_start=datetime.now() - timedelta(days=365),
            reporting_period_end=datetime.now(),
            ai_insights=self._generate_ai_insights(overall_score, ubuntu_score, organization),
            improvement_areas=self._identify_improvement_areas(
                env_score, social_score, governance_score, ubuntu_score
            )
        )
        
        return esg_score
    
    def _calculate_environmental_score(
        self, 
        env_data: Dict[str, Any], 
        organization: Organization
    ) -> float:
        """Calculate environmental performance score"""
        
        score = 0.0
        max_score = 100.0
        
        # Carbon emissions performance (30%)
        carbon_score = self._assess_carbon_performance(env_data.get("carbon_data", {}))
        score += carbon_score * 0.30
        
        # Renewable energy usage (25%)
        renewable_score = self._assess_renewable_energy(env_data.get("energy_data", {}))
        score += renewable_score * 0.25
        
        # Water management (20%)
        water_score = self._assess_water_management(env_data.get("water_data", {}))
        score += water_score * 0.20
        
        # Waste management (15%)
        waste_score = self._assess_waste_management(env_data.get("waste_data", {}))
        score += waste_score * 0.15
        
        # Biodiversity and conservation (10%)
        biodiversity_score = self._assess_biodiversity_impact(env_data.get("biodiversity_data", {}))
        score += biodiversity_score * 0.10
        
        return min(score, max_score)
    
    def _calculate_social_score(
        self, 
        social_data: Dict[str, Any], 
        organization: Organization
    ) -> float:
        """Calculate social performance score"""
        
        score = 0.0
        max_score = 100.0
        
        # Employee wellbeing and safety (25%)
        employee_score = self._assess_employee_wellbeing(social_data.get("employee_data", {}))
        score += employee_score * 0.25
        
        # Community relations (25%)
        community_score = self._assess_community_relations(social_data.get("community_data", {}))
        score += community_score * 0.25
        
        # Diversity and inclusion (20%)
        diversity_score = self._assess_diversity_inclusion(social_data.get("diversity_data", {}))
        score += diversity_score * 0.20
        
        # Human rights and labor practices (20%)
        rights_score = self._assess_human_rights(social_data.get("rights_data", {}))
        score += rights_score * 0.20
        
        # Supply chain responsibility (10%)
        supply_chain_score = self._assess_supply_chain_responsibility(social_data.get("supply_chain_data", {}))
        score += supply_chain_score * 0.10
        
        return min(score, max_score)
    
    def _calculate_governance_score(
        self, 
        governance_data: Dict[str, Any], 
        organization: Organization
    ) -> float:
        """Calculate governance performance score"""
        
        score = 0.0
        max_score = 100.0
        
        # Board composition and independence (25%)
        board_score = self._assess_board_composition(governance_data.get("board_data", {}))
        score += board_score * 0.25
        
        # Transparency and disclosure (25%)
        transparency_score = self._assess_transparency(governance_data.get("transparency_data", {}))
        score += transparency_score * 0.25
        
        # Anti-corruption and ethics (20%)
        ethics_score = self._assess_ethics_anticorruption(governance_data.get("ethics_data", {}))
        score += ethics_score * 0.20
        
        # Risk management (15%)
        risk_score = self._assess_risk_management(governance_data.get("risk_data", {}))
        score += risk_score * 0.15
        
        # Stakeholder engagement (15%)
        stakeholder_score = self._assess_stakeholder_engagement(governance_data.get("stakeholder_data", {}))
        score += stakeholder_score * 0.15
        
        return min(score, max_score)
    
    def _calculate_community_engagement(
        self, 
        community_activities: Dict[str, Any],
        community_data: Dict[str, Any]
    ) -> float:
        """Calculate community engagement score for Ubuntu Index"""
        
        score = 0.0
        
        # Regular community consultations
        if community_activities.get("regular_consultations", False):
            score += 25
        
        # Community development projects
        projects = community_activities.get("development_projects", [])
        if len(projects) >= 3:
            score += 30
        elif len(projects) >= 1:
            score += 20
        
        # Local hiring and training
        local_hiring_rate = community_activities.get("local_hiring_percentage", 0)
        if local_hiring_rate >= 80:
            score += 25
        elif local_hiring_rate >= 60:
            score += 20
        elif local_hiring_rate >= 40:
            score += 15
        
        # Community feedback incorporation
        if community_activities.get("feedback_mechanism", False):
            score += 20
        
        return min(score, 100.0)
    
    def _calculate_local_procurement(self, procurement_data: Dict[str, Any]) -> float:
        """Calculate local procurement score for Ubuntu Index"""
        
        local_percentage = procurement_data.get("local_supplier_percentage", 0)
        
        if local_percentage >= 70:
            return 100.0
        elif local_percentage >= 50:
            return 85.0
        elif local_percentage >= 30:
            return 70.0
        elif local_percentage >= 15:
            return 50.0
        else:
            return 25.0
    
    def _calculate_cultural_preservation(self, cultural_data: Dict[str, Any]) -> float:
        """Calculate cultural preservation score for Ubuntu Index"""
        
        score = 0.0
        
        # Support for local cultural events
        if cultural_data.get("supports_cultural_events", False):
            score += 30
        
        # Preservation of historical sites
        if cultural_data.get("heritage_preservation", False):
            score += 25
        
        # Support for local languages
        if cultural_data.get("multilingual_services", False):
            score += 25
        
        # Traditional knowledge recognition
        if cultural_data.get("traditional_knowledge_respect", False):
            score += 20
        
        return min(score, 100.0)
    
    def _calculate_indigenous_knowledge_integration(
        self, 
        indigenous_data: Dict[str, Any]
    ) -> float:
        """Calculate indigenous knowledge integration score"""
        
        score = 0.0
        
        # Integration of traditional practices
        if indigenous_data.get("traditional_practices_integrated", False):
            score += 40
        
        # Consultation with traditional leaders
        if indigenous_data.get("traditional_leader_consultation", False):
            score += 30
        
        # Documentation and preservation of knowledge
        if indigenous_data.get("knowledge_documentation", False):
            score += 30
        
        return min(score, 100.0)
    
    def _calculate_local_employment(self, employment_data: Dict[str, Any]) -> float:
        """Calculate local employment score"""
        
        local_employment_rate = employment_data.get("local_employment_percentage", 0)
        skills_development_programs = employment_data.get("skills_development", False)
        
        base_score = min(local_employment_rate, 100.0)
        
        # Bonus for skills development
        if skills_development_programs:
            base_score = min(base_score + 15, 100.0)
        
        return base_score
    
    def _calculate_community_investment(self, investment_data: Dict[str, Any]) -> float:
        """Calculate community investment score"""
        
        investment_percentage = investment_data.get("revenue_percentage_invested", 0)
        
        if investment_percentage >= 5:
            return 100.0
        elif investment_percentage >= 3:
            return 85.0
        elif investment_percentage >= 2:
            return 70.0
        elif investment_percentage >= 1:
            return 55.0
        elif investment_percentage > 0:
            return 40.0
        else:
            return 0.0
    
    def _generate_ai_insights(
        self, 
        overall_score: float, 
        ubuntu_score: float, 
        organization: Organization
    ) -> Dict[str, Any]:
        """Generate AI-powered insights based on ESG performance"""
        
        insights = {
            "performance_summary": f"Overall ESG score of {overall_score:.1f} with Ubuntu Index of {ubuntu_score:.1f}",
            "strengths": [],
            "opportunities": [],
            "recommendations": [],
            "african_context_rating": "High" if ubuntu_score > 70 else "Medium" if ubuntu_score > 40 else "Low"
        }
        
        # Add context-specific insights
        if ubuntu_score > 80:
            insights["strengths"].append("Strong Ubuntu philosophy integration")
        if overall_score > 75:
            insights["strengths"].append("Above-average ESG performance")
        
        if ubuntu_score < 50:
            insights["opportunities"].append("Enhance community engagement and local partnerships")
        if overall_score < 60:
            insights["opportunities"].append("Focus on systematic ESG improvements")
        
        return insights
    
    def _identify_improvement_areas(
        self, 
        env_score: float, 
        social_score: float, 
        governance_score: float, 
        ubuntu_score: float
    ) -> List[Dict[str, Any]]:
        """Identify specific areas for improvement"""
        
        improvements = []
        
        if env_score < 60:
            improvements.append({
                "area": "Environmental Performance",
                "priority": "High",
                "suggestions": ["Improve carbon management", "Increase renewable energy usage"]
            })
        
        if social_score < 60:
            improvements.append({
                "area": "Social Performance", 
                "priority": "High",
                "suggestions": ["Enhance employee wellbeing", "Strengthen community relations"]
            })
        
        if governance_score < 60:
            improvements.append({
                "area": "Governance",
                "priority": "Medium",
                "suggestions": ["Improve board diversity", "Enhance transparency"]
            })
        
        if ubuntu_score < 50:
            improvements.append({
                "area": "Ubuntu Philosophy",
                "priority": "High",
                "suggestions": ["Increase local procurement", "Enhance community engagement"]
            })
        
        return improvements
    
    # Additional helper methods for specific assessments
    def _assess_carbon_performance(self, carbon_data: Dict[str, Any]) -> float:
        """Assess carbon management performance"""
        # Implementation for carbon performance assessment
        return 75.0  # Placeholder
    
    def _assess_renewable_energy(self, energy_data: Dict[str, Any]) -> float:
        """Assess renewable energy usage"""
        renewable_percentage = energy_data.get("renewable_percentage", 0)
        return min(renewable_percentage * 2, 100.0)  # Scale to 100
    
    def _assess_water_management(self, water_data: Dict[str, Any]) -> float:
        """Assess water management practices"""
        # Implementation for water management assessment
        return 70.0  # Placeholder
    
    def _assess_waste_management(self, waste_data: Dict[str, Any]) -> float:
        """Assess waste management practices"""
        # Implementation for waste management assessment
        return 65.0  # Placeholder
    
    def _assess_biodiversity_impact(self, biodiversity_data: Dict[str, Any]) -> float:
        """Assess biodiversity and conservation impact"""
        # Implementation for biodiversity assessment
        return 60.0  # Placeholder
    
    def _assess_employee_wellbeing(self, employee_data: Dict[str, Any]) -> float:
        """Assess employee wellbeing and safety"""
        # Implementation for employee assessment
        return 80.0  # Placeholder
    
    def _assess_community_relations(self, community_data: Dict[str, Any]) -> float:
        """Assess community relations"""
        # Implementation for community relations assessment
        return 75.0  # Placeholder
    
    def _assess_diversity_inclusion(self, diversity_data: Dict[str, Any]) -> float:
        """Assess diversity and inclusion"""
        # Implementation for diversity assessment
        return 70.0  # Placeholder
    
    def _assess_human_rights(self, rights_data: Dict[str, Any]) -> float:
        """Assess human rights and labor practices"""
        # Implementation for human rights assessment
        return 85.0  # Placeholder
    
    def _assess_supply_chain_responsibility(self, supply_chain_data: Dict[str, Any]) -> float:
        """Assess supply chain responsibility"""
        # Implementation for supply chain assessment
        return 65.0  # Placeholder
    
    def _assess_board_composition(self, board_data: Dict[str, Any]) -> float:
        """Assess board composition and independence"""
        # Implementation for board assessment
        return 75.0  # Placeholder
    
    def _assess_transparency(self, transparency_data: Dict[str, Any]) -> float:
        """Assess transparency and disclosure"""
        # Implementation for transparency assessment
        return 80.0  # Placeholder
    
    def _assess_ethics_anticorruption(self, ethics_data: Dict[str, Any]) -> float:
        """Assess ethics and anti-corruption measures"""
        # Implementation for ethics assessment
        return 85.0  # Placeholder
    
    def _assess_risk_management(self, risk_data: Dict[str, Any]) -> float:
        """Assess risk management practices"""
        # Implementation for risk management assessment
        return 70.0  # Placeholder
    
    def _assess_stakeholder_engagement(self, stakeholder_data: Dict[str, Any]) -> float:
        """Assess stakeholder engagement"""
        # Implementation for stakeholder engagement assessment
        return 75.0  # Placeholder
    
    def _calculate_bee_compliance_score(self, organization: Organization, db: Session) -> float:
        """Calculate BEE compliance score for South African organizations"""
        if organization.country_code != "ZA":
            return 0.0  # Not applicable
        
        # Get latest BEE compliance record
        compliance_record = db.query(ComplianceRecord).filter(
            ComplianceRecord.organization_id == organization.id,
            ComplianceRecord.framework == "bee"
        ).order_by(ComplianceRecord.assessment_date.desc()).first()
        
        if compliance_record:
            return compliance_record.compliance_percentage
        
        return 0.0
    
    def _calculate_local_employment_score(self, social_data: Dict[str, Any]) -> float:
        """Calculate local employment score"""
        employment_data = social_data.get("employee_data", {})
        local_percentage = employment_data.get("local_employment_percentage", 0)
        return min(local_percentage, 100.0)
    
    def _calculate_community_investment_score(self, ubuntu_data: Dict[str, Any]) -> float:
        """Calculate community investment score"""
        investment_data = ubuntu_data.get("community_investment", {})
        return self._calculate_community_investment(investment_data)