from django.db import models

PROJECT_TYPE(
	('RESN':'Residential New Build'),
	('RESA':'Residential A&A'),
	('COMN':'Commercial New Build'),
	('COMA':'Commercial A&A'),
	('GOVN':'Government New Build'),
	('GOVA':'Government A&A'),
	('SCHN':'School New Build'),
	('SCHA':'School A&A'),
	('HOSN':'Hospital New Build'),
	('HOSA':'Hospital A&A'),
	('OTHN':'Others New Build'),
	('OTHA':'Others A&A'),
)

PROJECT_STATUS = (
	('PRE':'Pre-construction'),
	('ON': 'On-going'),
	('CMP':'Completion'),
)

BQ_STATUS = (
	('DFT':'Draft'),
	('PUB': 'Published'),
	('RESP':'Responded'),
	('IV':'In-review'),
	('CLS':'Closed'),
)

BQ_TRADE_CLASS = (
	('CW01':'CW01 General Building'),
	('CW02':'CW02 Civil Engineering'),
	('CR01':'CR01 Minor Construction Works'),
	('CR02':'CR02 Corrosion Protection'),
	('CR03':'CR03 Demolition'),
	('CR04':'CR04 Fencing & Ironworks'),
	('CR05':'CR05 Concrete Repair'),
	('CR06':'CR06 Interior Decoration & Finishing Works'),
	('CR07':'CR07 Cable/Pipe Laying & Road Reinstatement'),
	('CR08':'CR08 Piping Works'),
	('CR09':'CR09 Repair & Redecoration'),
	('CR10':'CR10 Pre-cast Concrete Works'),
	('CR11':'CR11 Sign Craft Installation'),
	('CR12':'CR12 Ground Support & Stabilization'),
	('CR13':'CR13 Waterproofing Installation'),
	('CR14':'CR14 Asphalt Works & Road Making'),
	('CR15':'CR15 Site Investigation'),
	('CR16':'CR16 Curtain Walls'),
	('CR17':'CR17 Windows'),
	('CR18':'CR18 Doors'),
	('MW02':'MW02 House Keeping, Cleansing, Desilting & Conservancy Services'),
	('MW03':'MW03 Landscaping'),
	('MW04':'Pest Control'),
	('ME01':'ME01 Air-condition, Refrigeration & Ventilation Works'),
	('ME02':'ME02 Building Automation, Industrial & Process Control System'),
	('ME03':'ME03 Solar PV System Integration'),
	('ME04':'ME04 Communication & Security System'),
	('ME05':'ME05 Electrical Engineering'),
	('ME06':'ME06 FIre Prevention & Protection System'),
	('ME07':'ME07 High & Low Tension Overhead Line Installation'),
	('ME08':'ME08 Internal Telephone Wiring for Telecommunication'),
	('ME09':'ME09 Lift & Escalator Installation'),
	('ME10':'ME10 Line Plant Cabling/Wiring for Telecommunication'),
	('ME11':'ME11 Mechanical Engineering'),
	('ME12':'ME12 Plumbing & Sanitary Works'),
	('ME13':'ME13 Traffic Light System'),
	('ME14':'ME14 Underground Pileline for Telecommunication'),
	('ME15':'ME15 Integrated Building Services'),
	('RW00':'RW00 Eligible Workhead'), 
	('RW01':'RW01 Window Contractor'),
	('RW02':'RW02 Lift Contractor'),
	('SY01A':'SY01A Essential Construction Material'),
	('SY01B':'SY01B Ready-Mixed Concrete'),
	('SY01C':'SY01C Other Basic Construction Material'),
	('SY02':'SY02 Chemicals'),
	('SY04':'SY04 Electrical Equipment'),
	('SY05':'SY05 Electrical & ELectronic Materials, Products & Components'),
	('SY06':'SY06 Finishing & Building Products'),
	('SY07':'SY07 Gases'),
	('SY08':'SY08 Mechanical Equipment, Plant & Machinery'),
	('SY09':'SY09 Mechanical Materials, Products & Components'),
	('SY10':'SY10 Metal & Timber Structures'),
	('SY11':'SY11 Petroleum Products'),
	('SY12':'SY12 Pipes'),
	('SY14':'SY14 Sanitary Pipes'),
	('TR01':'TR01 Formwork'),
	('TR02':'TR02 Steel Reinforcement Works'),
	('TR03':'TR03 Concreting Works'),
	('TR04':'TR04 Drywall Installation'),
	('TR05':'TR05 Pre-cast Installation'),
	('TR06':'TR06 Ceiling Work'),
	('TR07':'TR07 Tile/Marble/Stone Works'),
	('TR08':'TR08 Timber Flooring Works'),
	('TR09':'TR09 Plastering / Skimming'),
	('TR10':'TR10 Ironmongery & Metal Works'), 
	('OTHER':'Others'),
)


# Create your models here.
class BQ(models.Model):
	"""BQ model"""
	bq_name = models.CharField(max_length = 100)
	bq_status = models.CharField(max_length = 10, choices = BQ_STATUS)
	bq_description = models.TextField()
	bq_quantity = models.IntegerField()
	bq_start_date  = models.DateField()
	bq_end_date = models.DateField()
	bq_trade_class = models.CharField(max_length = 10, choices = BQ_TRADE_CLASS)
	project = models.ForeignKey(Project)

class Project(models.Model):
	"""Project model"""
	pj_name = models.CharField(max_length = 100)
	pj_type = models.CharField(max_length = 10, choices = PROJECT_TYPE)
	pj_status = models.CharField(max_length = 10, choices = PROJECT_STATUS)
	pj_description = models.TextField()
	pj_start_date  = models.DateField()
	pj_end_date = models.DateField()
	pj_location = models.CharField(max_length = 100)

		