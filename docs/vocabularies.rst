Vocabularies
------------------

In STIX 2.x, vocabularies are referred to as "open". Although
vocabularies in STIX 1.x were referred to as "controlled", the actual
difference between them is negligible. In both standards, vocabulary
literals were suggested, but not required to be used. Producers using
either standards are free to use any string as a value. The most
important difference is that in STIX 1.x it was possible to require that
only suggested literals were used, and have that enforced through XML
schema validation.

Certain STIX 2.x vocabularies are either copied verbatim from STIX 1.x,
or with few changes. Others, are revamped in STIX 2.x, and it might be
difficult to find a corresponding literal to one from STIX 1.x. However,
because all of these vocabularies are open in STIX 2.x, those values can
be used directly.

+------------------------------------------+-----------------------------------+
| **STIX 1.x Vocabulary**                  | **STIX 2.x Vocabulary**           |
+==========================================+===================================+
| ``AssetTypeVocab``                       | *not available in STIX 2.x*       |
+------------------------------------------+-----------------------------------+
| ``AttackerInfrastructureTypeVocab``      | *not available in STIX 2.x*       |
+------------------------------------------+-----------------------------------+
| ``AttackerToolTypeVocab``                | ``tool-label-ov``                 |
+------------------------------------------+-----------------------------------+
| ``AvailabilityLossTypeVocab``            | *not available in STIX 2.x*       |
+------------------------------------------+-----------------------------------+
| ``COAStageVocab``                        | *not available in STIX 2.x*       |
+------------------------------------------+-----------------------------------+
| ``CampaignStatusVocab``                  | *not available in STIX 2.x*       |
+------------------------------------------+-----------------------------------+
| ``CourseOfActionTypeVocab``              | ``course-of-action-label-ov``     |
+------------------------------------------+-----------------------------------+
| ``DiscoveryMethodVocab``                 | *not available in STIX 2.x*       |
+------------------------------------------+-----------------------------------+
| ``HighMediumLowVocab``                   | *not used*                        |
+------------------------------------------+-----------------------------------+
| ``ImpactQualificationVocab``             | *not available in STIX 2.x*       |
+------------------------------------------+-----------------------------------+
| ``ImpactRatingVocab``                    | *not available in STIX 2.x*       |
+------------------------------------------+-----------------------------------+
| ``IncidentCategoryVocab``                | *not available in STIX 2.x*       |
+------------------------------------------+-----------------------------------+
| ``IncidentEffectVocab``                  | *not available in STIX 2.x*       |
+------------------------------------------+-----------------------------------+
| ``IncidentStatusVocab``                  | *not available in STIX 2.x*       |
+------------------------------------------+-----------------------------------+
| ``IndicatorTypeVocab``                   | ``indicator-label-ov``            |
+------------------------------------------+-----------------------------------+
| ``InformationSourceRoleVocab``           | *not available in STIX 2.x*       |
+------------------------------------------+-----------------------------------+
| ``InformationTypeVocab``                 | *not available in STIX 2.x*       |
+------------------------------------------+-----------------------------------+
| ``IntendedEffectVocab``                  | ``attack-objective-ov``           |
+------------------------------------------+-----------------------------------+
| ``LocationClassVocab``                   | *not available in STIX 2.x*       |
+------------------------------------------+-----------------------------------+
| ``LossDurationVocab``                    | *not available in STIX 2.x*       |
+------------------------------------------+-----------------------------------+
| ``LossPropertyVocab``                    | *not available in STIX 2.x*       |
+------------------------------------------+-----------------------------------+
| ``MalwareTypeVocab``                     | ``malware-label-ov``              |
+------------------------------------------+-----------------------------------+
| ``ManagementClassVocab``                 | *not available in STIX 2.x*       |
+------------------------------------------+-----------------------------------+
| ``MotivationVocab``                      | ``attack-motivation-ov``          |
+------------------------------------------+-----------------------------------+
| ``OwnershipClassVocab``                  | *not available in STIX 2.x*       |
+------------------------------------------+-----------------------------------+
| ``PackageIntentVocab``                   | *not used*                        |
+------------------------------------------+-----------------------------------+
| ``PlanningAndOperationalSupportVocab``   | ``resource-level-ov``             |
+------------------------------------------+-----------------------------------+
| ``ReportIntentVocab``                    | ``report-label-ov``               |
+------------------------------------------+-----------------------------------+
| ``SecurityCompromiseVocab``              | *not used*                        |
+------------------------------------------+-----------------------------------+
| ``SystemTypeVocab``                      | *not available in STIX 2.x*       |
+------------------------------------------+-----------------------------------+
| ``ThreatActorSophisticationVocab``       | ``attack-sophistication-level-ov``|
+------------------------------------------+-----------------------------------+
| ``ThreatActorTypeVocab``                 | ``threat-actor-label-ov``         |
+------------------------------------------+-----------------------------------+
| ``VersioningVocab``                      | *not used*                        |
+------------------------------------------+-----------------------------------+

New vocabularies added in STIX 2.x are:

-  ``attack-resource-level-ov``

-  ``encryption-algo-ov``

-  ``hash-algorithm-ov``

-  ``identity-class-ov``

-  ``industry-sector-ov``

-  ``marking-definition-ov``

-  ``threat-actor-role-ov``

-  ``windows-pebinary-type-ov``

In addition, the STIX 2.x specification contains enumerations. These are
mostly for cyber observables. These are different from open vocabularies
because only values explicitly defined in the enumeration can be used.
The enumerations defined in STIX 2.x are:

-  ``network-socket-type-enum``

-  ``windows-service-start-type-enum``

-  ``windows-service-status-enum``

-  ``windows-service-type-enum``

which correspond to similar enumerations defined in STIX 1.x.
