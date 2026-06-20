# Payment Rails & Clearings

> Source: https://docs.temenos.com/docs/Solutions/Payments/Packages/Payment_Packages/Packages/Payment_Packages/Clearing.htm

---

2. [Payments](../../../../content/payments.html)
3. You are here:
   Payment Packages > Payment Rails & Clearings

- Payment Packages;)
  - [Overview](../../Packages/Misc/Overview.htm)
  - [Payments Platform](../../Packages/Payment_Packages/Platform.htm)
  - [Payment Rails & Clearings](../../Packages/Payment_Packages/Clearing.htm)
  - [SWIFT Payments](../../Packages/Payment_Packages/SWIFT.htm)
  - [Payments Repair](../../Packages/Payment_Packages/Repair.htm)

Payments

# Payment Rails & Clearings

Updated On 12 April 2026 |
 2 Min(s) read

Feedback
Summarize

Payment Rails and Clearings provide optional, scheme‑specific capabilities that extend the Payments Platform to support domestic and regional payment networks. Clients license these capabilities independently from the core Payments Platform and may combine multiple rails or clearings across regions and schemes to align with their market footprint and local clearing requirements.

Payment Rails and Clearings enable clients to:

- Extend core payments processing to specific domestic or regional clearing schemes.
- Support localized processing rules, including cut‑off times, settlement cycles, and scheme‑specific payment flows.

## End‑to‑End Rails vs Clearing Frameworks

Temenos supports payment rails and clearings in two ways:

- **End to end Temenos Clearing Offerings**

  Where Temenos provides an off the shelf clearing or payment rail, clients can license the corresponding clearing or rail directly to enable end to end processing for that scheme.
- **Clearing Framework–based Enablement**

  For clearing schemes that are not available off the shelf, clients can license the Payment Clearing Framework bundle, which provides the foundational orchestration and configuration capabilities required to develop and support country or region specific clearings.

## Payments Clearing Framework Bundle (PMT-CLR-FRW)

The Payment Clearing Framework bundle (PMT-CLR-FRW) delivers a reusable orchestration layer and standardized configuration patterns to support domestic and regional clearing implementations.

The bundle supports:

- Clearing‑specific orchestration and processing flows.
- Configuration of local rules, cut‑off times, and settlement patterns.
- Extensibility to build and operate country‑ or scheme‑specific clearings as required.

Clients may license one or more clearing frameworks (for example, Instant Payments, ACH, RTGS, or Request to Pay) based on their clearing landscape and regulatory requirements.

| Module Code | Module Name |
| --- | --- |
| RF | [Request to Pay Framework](../../../../Payments/RF/Request_to_Pay/MISC/Introduction.htm) |
| PPACHF | [ACH Payments Framework](../../../../Payments/PP/Payments_Hub_(PP)/Clearing/Configuration.htm#PPACHF) |
| PPRTGF | [RTGS Payments Framework](../../../../Payments/PP/Payments_Hub_(PP)/Clearing/Configuration.htm#RTGS) |
| PPINST | [Instant Payment Framework](../../../../Payments/PP/Payments_Hub_(PP)/Instant_Payments/Introduction.htm) |

## Dependency

Payments Platform bundle is required (PMT-BASE, PMT-ADV or PMT-PREM).

In this topic

- [Payment Rails & Clearings](#PaymentRailsClearings)

- [End‑to‑End Rails vs Clearing Frameworks](#EndtoEndRailsvsClearingFrameworks)
- [Payments Clearing Framework Bundle (PMT-CLR-FRW)](#PaymentsClearingFrameworkBundlePMTCLRFRW)
- [Dependency](#Dependency)




Copyright © 2020-2026 Temenos Headquarters SA

Cookies Settings;)[Privacy Policy](https://www.temenos.com/legal-information/privacy-policy/)[Cookie Policy](/cookie-policy.html)

###### Contact Us

[knowledge@temenos.com](mailto:knowledge@temenos.com?subject=Contact Us)

Published on :
Tuesday, April 14, 2026 6:11:30 PM IST