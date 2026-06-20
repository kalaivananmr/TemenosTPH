# SWIFT Bundles – Overview (Conceptual)

> Source: https://docs.temenos.com/docs/Solutions/Payments/Packages/Payment_Packages/Packages/Payment_Packages/SWIFT.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Payment Packages > SWIFT Payments

- Payment Packages;)
  - [Overview](../../Packages/Misc/Overview.htm)
  - [Payments Platform](../../Packages/Payment_Packages/Platform.htm)
  - [Payment Rails & Clearings](../../Packages/Payment_Packages/Clearing.htm)
  - [SWIFT Payments](../../Packages/Payment_Packages/SWIFT.htm)
  - [Payments Repair](../../Packages/Payment_Packages/Repair.htm)

Payments

# SWIFT Bundles – Overview (Conceptual)

Updated On 12 April 2026 |
 3 Min(s) read

Feedback
Summarize

SWIFT Bundles (PMT-SWIFT, PMT-SWIFT-PREM) SWIFT messaging, connectivity, and compliance components for cross border processing. The bundles include:

- ISO 20022 CBPR+ message support for payments and account statements.
- Exceptions & investigations handling aligned to CBPR+ processes.
- SWIFT connectivity via SWIFT Alliance connector for InterAct message exchange.

The differences between two SWIFT Bundles relate to:

- Optional SWIFT modules and advanced capabilities (extended CBPR+ message families such as Bank Claims & Charge Advices and Adhoc Charge Advices)
- SWIFT gpi enablement
- Connectivity options (SWIFT Alliance Cloud Connector)
- Operational automation (automated RMA and SSI uploads)

## SWIFT Bundle Variants – At a Glance (Positioning)

This section defines the scope and intended use of each SWIFT Bundle variant.

**PMT-SWIFT – SWIFT Payments Standard**

- Core ISO 20022 CBPR+ capabilities for payments and account statements
- CBPR+ exceptions and investigations handling
- SWIFT Alliance connector for InterAct message exchange (On-Prem)

**PMT-SWIFT-PREM – SWIFT Payments Advanced**

- Includes all Standard capabilities (CBPR+, exceptions/investigations, Alliance connector)
- Extended CBPR+ message families (e.g., Bank Claims & Charge Advices, Adhoc Charge Advices, cheques)
- SWIFT gpi support
- SWIFT Alliance Cloud Connector option
- Automated RMA and SSI uploads for operational efficiency

## Functional Coverage Comparison

This section outlines the module coverage across the SWIFT bundles.

[ SWIFT Bundle Coverage Matrix](#)

This matrix provides a side-by-side view of module coverage across the SWIFT bundles (PMT-SWIFT and PMT-SWIFT-PREM). Each row lists a module code and module name, and the checkmarks indicate which bundle includes that capability—highlighting the baseline CBPR+ coverage in SWIFT Payments Standard and the additional capabilities in SWIFT Payments Advanced.

| Module Code | Module Name | PMT-SWIFT | PMT-SWIFT-PREM |
| --- | --- | --- | --- |
| DEMXTR | [Delivery MX Translation](../../../../../T24_Transact/Customer_Output/DEMXTR/Delivery_MX_Translation/Misc/Introduction.htm) |  |  |
| ER | [Expected Receipts](../../../../../T24_Transact/Reconciliation_Matching/ER/Expected_Recs/Misc/Introduction.htm) |  |  |
| PPSWCR | [SWIFT CBPR+ Recalls, Returns and Resolution of Investigation](../../../../International_Payments/PPSWCR/International_PaymentsCBPR/PPSWCR/Introduction.htm) |  |  |
| PPSWEI | [SWIFT Exceptions & Investigations](../../../../International_Payments/PPSWEI/International_PaymentsCBPR/PPSWEI/Introduction.htm) |  |  |
| PPSWMX | [SWIFT CBPR+ ISO20022 Payments (Phase I - March 2023)](../../../../International_Payments/PPSWMX/International_PaymentsCBPR/PPSWMX/Introduction.htm) |  |  |
| SF | [SWIFT MT Message Enablement](../../../../Payments/PP/Payments_Hub_(PP)/International_Payments/Introduction.htm) |  |  |
| PSINCV | [Payments Shared International Country Validations](../../../../Payments/PSINCV/Country_Validation/Misc/Introduction.htm) |  |  |
| SWFTAL | [SWIFT Alliance Interface](../../../../../Regionalized_Solutions/Global_Model_Bank/SWFTAL/Global_ModelBank/Swift_Alliance_Interface/Introduction.htm) |  |  |
| SWFTCO | [T24 SWIFT Interac connector](../../../../../Ecosystem/Core_Banking_and_infrastructure/Interfaces/Swift_Interface/Swift_Interface_Features/Overview.htm) |  |  |
| IZ | [Account Reporting Events & Services](../../../../../Technology/Microservices/IZCAMT/Account_Reporting_Events_and_Services/Misc/Introduction.htm) |  |  |
| IZEMBD | [ISO20022 Outward CamtAccount Reporting - (Transact Embedded)](../../../../../T24_Transact/Customer_Output/IZEMBD/Embedded_ISO20022/Misc/Introduction.htm) |  |  |

[Modules Exclusive or Enhanced in Higher Packages](#)

| Module Code | Module Name | PMT-SWIFT | PMT-SWIFT-PREM |
| --- | --- | --- | --- |
| PPSWCL | [SWIFT CBPR+ (MX) Bank Claims & Charge Advices](../../../../International_Payments/PPSWCL/International_PaymentsCBPR/PPSWCL/Introduction.htm) | - |  |
| CGSWMX | [SWIFT CBPR+ (MX) Adhoc Charge Advices](../../../../International_Payments/CGSWMX/International_PaymentsCBPR/CGSWMX/Introduction.htm) | - |  |
| PPSSIU | [SWIFT SSI Upload](../../../../International_Payments/PPSSIU/International_PaymentsCBPR/PPSSIU/Introduction.htm) | - |  |
| PPSWCQ | [SWIFT CBPR+ Cheques](../../../../International_Payments/PPSWCQ/International_PaymentsCBPR/PPSWCQ/Introduction.htm) | - |  |
| PPSGPI | [SWIFT GPI](../../../../../T24_Transact/Framework/RD/CRD/SWIFT_Gpi_Directory/Introduction.htm) | - |  |
| SFRAAD | [SWIFT RMA Adapter](../../../../../Installation/SWIFT_RMA_Upload_Adapter/SWIFT_RMA_Upload_Adapter/Misc/Overview.htm) | - |  |
|
|
|
| SWFTGPI | [SWIFT GPI Adaptor](../../../../Payments/PP/Payments_Hub_(PP)/Swift_GPI/Introduction.htm) | - |  |

## Dependencies & Deployment Notes

- A Payments Platform bundle is required (One of PMT-BASE, PMT-ADV or PMT-PREM)
- IZEMBD works only with Embedded Payments with Transact (PMT-BASE or PMT-ADV only)

In this topic

- [SWIFT Bundles – Overview (Conceptual)](#SWIFTBundlesOverviewConceptual)

- [SWIFT Bundle Variants – At a Glance (Positioning)](#SWIFTBundleVariantsAtaGlancePositioning)
- [Functional Coverage Comparison](#FunctionalCoverageComparison)
- [Dependencies & Deployment Notes](#DependenciesDeploymentNotes)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 6:11:31 PM IST