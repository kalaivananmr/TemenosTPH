# Platform Bundles – Overview (Conceptual)

> Source: https://docs.temenos.com/docs/Solutions/Payments/Packages/Payment_Packages/Packages/Payment_Packages/Platform.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Payment Packages > Payments Platform

- Payment Packages;)
  - [Overview](../../Packages/Misc/Overview.htm)
  - [Payments Platform](../../Packages/Payment_Packages/Platform.htm)
  - [Payment Rails & Clearings](../../Packages/Payment_Packages/Clearing.htm)
  - [SWIFT Payments](../../Packages/Payment_Packages/SWIFT.htm)
  - [Payments Repair](../../Packages/Payment_Packages/Repair.htm)

Payments

# Platform Bundles – Overview (Conceptual)

Updated On 12 April 2026 |
 4 Min(s) read

Feedback
Summarize

The Payments Platform Bundles (PMT-BASE, PMT-ADV, and PMT-PREM) form the core payments processing foundation for all Payments implementations.

**Common Capabilities Across All Platform Bundles**

All Platform Bundles provide the following baseline capabilities:

- Core payment processing
- Routing and orchestration
- Configuration-driven business rules
- Operational controls and monitoring

The differences between Platform Bundles relate to:

- Processing scale and volume
- Complexity of business rules
- Deployment model (embedded vs standalone)
- Automated return handling
- Automated cancel of payment initiations
- Advanced option for filtering response handling
- Risk filtering

## Platform Bundle Variants – At a Glance (Positioning)

This section defines the scope and intended use of each Platform Bundle variant.

**PMT-BASE – Payments Platform Standard**

- Lightweight, embedded with Temenos Transact
- Low volumes, limited exception handling
- ISO 20022 compliant
- Suitable for simpler payment landscapes

**PMT-ADV – Payments Platform Advanced (PH Embedded)**

- High volume, complex interbank payments
- Advanced STP, SLAs, codeword based processing
- Unlimited clearings and formats
- Includes Payments Cockpit

**PMT-PREM – Enterprise Universal Payments**

- Embedded or standalone deployment
- Supports third party cores
- Enterprise scale volumes and complexity
- Full operational tooling and standalone capability

## Functional Coverage Comparison

This section outlines the module coverage across the Payments Platform bundles.

[ Platform Bundle Coverage Matrix](#)

This matrix presents a clear, side-by-side comparison of module coverage across the Payments Platform bundles—PMT-BASE, PMT-ADV, and PMT-PREM. Each row identifies a module by code and name, while the checkmarks indicate inclusion within each package, enabling quick visibility into baseline capabilities and highlighting where additional functionality is introduced at higher tiers.

| Module Code | Module Name | PMT-BASE | PMT-ADV | PMT-PREM |
| --- | --- | --- | --- | --- |
| BY | [Beneficiary](../../../../../T24_Transact/Framework/BY/Payments_Beneficiary/Misc/Introduction.htm) |  |  |  |
| BU | [Bulk Payment Order](../../../../Orders/PI/Payment_Initiation_(PI)/Bulk_Payments/Introduction.htm) |  |  |  |
| CG | [Charges](../../../../../T24_Transact/Framework/CG/Charges_and_Fees/Misc/Introduction.htm) |  |  |  |
| CQ | [Cheques and Cards Management](../../../../../T24_Transact/Accounts/AC_CQ/Cheque_Draft_Issue_Management/Misc/Introduction.htm) |  |  |  |
| CA | [Clearing Directory](../../../../../Payments/Payments/CA/Clearing_Directory_(CA)/Misc/Introduction.htm) |  |  |  |
| DE | [Delivery](../../../../../T24_Transact/Customer_Output/DE/Delivery/Misc/Introduction.htm) |  |  |  |
| DD | [Direct Debits](../../../../Payments/PP/Payments_Hub_(PP)/Direct_Debits/Introduction.htm) |  |  |  |
| PPFATF | [FATF Regulation](../../../../Payments/PP/Payments_Hub_(PP)/FATF/Introduction.htm) |  |  |  |
| IN | [IBAN](../../../../../T24_Transact/Framework/IN/IBAN/Misc/Introduction.htm) |  |  |  |
| RD | [Centralised Reference Data](../../../../../T24_Transact/Framework/RD/CRD/Misc/Introduction.htm) |  |  |  |
| SFRD25 | [SWIFT Identifiers Directory Upload](../../../../../T24_Transact/Framework/SFRD25/SFRD25/Misc/Introduction.htm) |  |  |  |
| PPISOX | [ISO20022 messages transforms](../../../../../T24_Transact/Customer_Output/DEMXTR/Delivery_MX_Translation/Misc/Introduction.htm) |  |  |  |
| PI | [Payment Initiation](../../../../Orders/PI/Payment_Initiation_(PI)/Misc/Introduction_PI.htm) |  |  |  |
| MX | [MX Payment Order](../../../../../T24_Transact/Customer_Output/DEMXTR/Delivery_MX_Translation/Transform_messages_to_Payment/Introduction.htm) |  |  |  |
| PP | [Payments](../../../../../Payments/Payments/PH/Payment_Suite_(PH)/PI_Vs_TPH/Payments_Initiation_PI_vs.htm) |  |  |  |
| PEMINT | [Payments External Messaging Interface](../../../../../Installation/TPH_Interfaces/TPH_Interfaces/Misc/Introduction.htm) |  |  |  |
| PPPSDC | [PSD2 Payments Transparency](../../../../Payments/PP/Payments_Hub_(PP)/PSD2_PPPSDC/Introduction.htm) |  |  |  |
| QA | [Queries and Answers](../../../../../T24_Transact/Framework/QA/Enquiries_and_Investigation/Enquiries_and_Investigations_for_SWIFT_MT_Messages/Introduction.htm?tocpath=Enquiries%20and%20Investigations%7CEnquiries%20and%20Investigations%20for%20SWIFT%20MT%20Messages%7C_____1#) |  |  |  |
| TZ | [Transaction Restrictions](../../../../../T24_Transact/Accounts/TZ/Transaction_Restriction/Misc/Introduction.htm) |  |  |  |
| PY | [Party Contact Address Management](../../../../../Technology/Microservices/Party/Party/Misc/Party.html) |  |  |  |
| PF | [Contact preferences](../../../../../T24_Transact/Customer_Output/DE/Delivery/Contact_Preferences/Introduction.htm) |  |  |  |
| PYBK | [Book Transfers](../../../../Payments/PP/Payments_Hub_(PP)/Book_Transfer/Introduction.htm) |  |  |  |

[Modules Exclusive or Enhanced in Higher Packages](#)

| Module Code | Module Name | PMT-BASE | PMT-ADV | PMT-PREM |
| --- | --- | --- | --- | --- |
| PH | [Payments Hub](../../../../Payments/PP/Payments_Hub_(PP)/Misc/Introduction.htm) | - |  |  |
| DB | [Direct Debit Collection Initiation](../../../../Payments/PP/Payments_Hub_(PP)/Direct_Debits/Introduction.htm) | - |  |  |
| PPUAGT | [Payments Cockpit](../../../../User_Agent/Payments_Operations_User_Agent/Payments_Operations_User_Agent/Introduction.htm) | - |  |  |
| LQ | [Liquidity Transfers & Advices Framework](../../../../Payments/LQ/Liquidity_Transfer_Advice_(LQ)/Liquidity_Transfer_Advice/Introduction.htm) | - |  |  |
| PPSTAL | [Standalone Payments](../../../../Payments/PP/Payments_Hub_(PP)/Standalone_Payments/Introduction.htm) | - | - |  |
| AC | [Accounts (AC) – Optional](../../../../../T24_Transact/Accounts/AC/Accounts/Misc/Introduction.htm) | - | - |  |
| MSSSHL | [Holdings – Optional](../../../../../Technology/Microservices/Holdings/holdings/holdings.htm) | - | - |  |
| MSSSPT | [Party MS – Optional](../../../../../Technology/Microservices/Party/Party/Misc/Party.html) | - | - |  |

## Dependencies & Deployment Notes

- Transact Platform is required for PMT-BASE & PMT-ADV
- TBC Infra Platform is required for PMT-PREM (Standalone deployments)

## Optional Add Ons & Examples

The Payments Platform supports a flexible set of optional extensions that can be added based on processing scope and market requirements.

**Compatible Extensions**

- SWIFT bundles (Standard or Advanced)
- Clearing frameworks such as RTGS, ACH, and Instant Payments
- Any supported domestic or scheme-based payment rail/clearing
- Payments Repair Bundle

- Platform Advanced + SWIFT Standard + RTGS rail/clearing
- Platform Advanced + Instant Payments rail/clearing (no SWIFT)
- Platform Standard + ACH Payments Framework
- Enterprise Universal Payment (standalone) + SWIFT Advanced + multiple domestic rails/clearings + Payments Repair Enterprise

In this topic

- [Platform Bundles – Overview (Conceptual)](#PlatformBundlesOverviewConceptual)

- [Platform Bundle Variants – At a Glance (Positioning)](#PlatformBundleVariantsAtaGlancePositioning)
- [Functional Coverage Comparison](#FunctionalCoverageComparison)
- [Dependencies & Deployment Notes](#DependenciesDeploymentNotes)
- [Optional Add Ons & Examples](#OptionalAddOnsExamples)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 6:11:30 PM IST