gt1_transform = {\
         'set_id': (1, None),
         'guarantor_number': (2, None),
         'guarantor_name': (3, None),
         'guarantor_spouse_name': (4, None),
         'guarantor_address': (5, None),
         'guarantor_phone__home': (6, None),
         'guarantor_phone__business': (7, None),
         'guarantor_date_of_birth': (8, datetransform),
         'guarantor_sex': (9, None),
         'guarantor_type': (10, None),
         'guarantor_relationship': (11, None),
         'guarantor_ssn': (12, None),
         'guarantor_date__begin': (13, datetransform),
         'guarantor_date__end': (14, datetransform),
         'guarantor_priority': (15, None),
         'guarantor_employer_name': (16, None),
         'guarantor_employer_addr': (17, None),
         'guarantor_employer_phone': (18, None),
         'guarantor_employee_id_': (19, None),
         'guarantor_employmt_status': (20, None),
               }

fhs_transform = {\
         'file_field_separators': (1, None),
         'file_encoding_characters': (2, None),
         'file_sending_application': (3, None),
         'file_sending_facility': (4, None),
         'file_rcving_application': (5, None),
         'file_receiving_facility': (6, None),
         'file_creation_datetime': (7, None),
         'file_security': (8, None),
         'file_nameidtype': (9, None),
         'file_comment': (10, None),
         'file_control_id': (11, None),
         'reference_file_cntrl_id': (12, None),
               }

rx1_transform = {\
         'unused': (1, None),
         'unused': (2, None),
         'route': (3, None),
         'site_administered': (4, None),
         'iv_solution_rate': (5, None),
         'drug_strength': (6, None),
         'final_concentration': (7, None),
         'final_volume_in_ml': (8, None),
         'drug_dose': (9, None),
         'drug_role': (10, None),
         'prescription_sequence_num': (11, None),
         'quantity_dispensed': (12, None),
         'unused': (13, None),
         'drug_id': (14, None),
         'component_drug_ids': (15, None),
         'prescription_type': (16, None),
         'substitution_status': (17, None),
         'rx_order_status': (18, None),
         'number_of_refills': (19, None),
         'unused': (20, None),
         'refills_remaining': (21, None),
         'dea_class': (22, None),
         'ordering_mds_dea_number': (23, None),
         'unused': (24, None),
         'last_refill_datetime': (25, None),
         'rx_number': (26, None),
         'prn_status': (27, None),
         'pharmacy_instructions': (28, None),
         'patient_instruction': (29, None),
         'instructions_sig': (30, None),
               }

obx_transform = {\
         'set_id': (1, None),
         'value_type': (2, None),
         'observation_identifier': (3, None),
         'observation_subid': (4, None),
         'observation_results': (5, None),
         'units': (6, None),
         'reference_range': (7, None),
         'abnormal_flags': (8, None),
         'probability': (9, None),
         'nature_of_abnormal_test': (10, None),
         'observ_result_status': (11, None),
         'date_last_normal_value': (12, None),
               }

qrf_transform = {\
         'where_subject_filter': (1, None),
         'when_data_start_datetime': (2, None),
         'when_data_end_datetime': (3, None),
         'what_user_qualifier': (4, None),
         'other_qry_subject_filter': (5, None),
               }

dsc_transform = {\
         'continuation_pointer': (1, None),
               }

pid_transform = {\
         'set_id': (1, None),
         'patient_id_external_id': (2, None),
         'patient_id_internal_id': (3, None),
         'alternate_patient_id': (4, None),
         'patients_name': (5, None),
         'mothers_maiden_name': (6, None),
         'date_of_birth': (7, datetransform),
         'sex': (8, None),
         'patient_alias': (9, None),
         'ethnic_group': (10, None),
         'patient_address': (11, None),
         'county_code': (12, None),
         'phone_number__home': (13, None),
         'phone_number__business': (14, None),
         'language__patient': (15, None),
         'marital_status': (16, None),
         'religion': (17, None),
         'patient_account_number': (18, None),
         'ssn_number__patient': (19, None),
         'drivers_license__patient': (20, None),
               }

acc_transform = {\
         'accident_datetime': (1, None),
         'accident_code': (2, None),
         'accident_location': (3, None),
               }

evn_transform = {\
         'event_type_code': (1, None),
         'datetime_of_event': (2, None),
         'datetime_planned_event': (3, None),
         'event_reason_code': (4, None),
               }

nte_transform = {\
         'set_id': (1, None),
         'source_of_comment': (2, None),
         'comment': (3, None),
               }

mrg_transform = {\
         'prior_patient_id__internal': (1, None),
         'prior_alt_patient_id': (2, None),
         'prior_patient_account_': (3, None),
               }

dsp_transform = {\
         'set_id': (1, None),
         'display_level': (2, None),
         'data_line': (3, None),
         'logical_break_point': (4, None),
         'result_id': (5, None),
               }

ub1_transform = {\
         'set_id': (1, None),
         'blood_deductible': (2, None),
         'blood_furnpints_of_40': (3, None),
         'blook_replacedpints_41': (4, None),
         'blood_not_rplcdpints42': (5, None),
         'coinsurance_days_25': (6, None),
         'condition_code': (7, None),
         'covered_days_23': (8, None),
         'noncovered_days_24': (9, None),
         'value_amount__code': (10, None),
         'number_of_grace_days_90': (11, None),
         'spec_prog_indicator44': (12, None),
         'psrour_approvl_ind_87': (13, None),
         'psrour_aprvd_stayfm88': (14, datetransform),
         'psrour_aprvd_stayto89': (15, datetransform),
         'occurrence_2832': (16, None),
         'occurrence_span_33': (17, None),
         'occur_span_start_date33': (18, datetransform),
         'occur_span_end_date_33': (19, datetransform),
         'ub82_locator_2': (20, None),
         'ub82_locator_9': (21, None),
         'ub82_locator_27': (22, None),
         'ub82_locator_45': (23, None),
               }

msh_transform = {\
         'field_separator': (1, None),
         'encoding_characters': (2, None),
         'sending_application': (3, None),
         'sending_facility': (4, None),
         'receiving_application': (5, None),
         'receiving_facility': (6, None),
         'datetime_of_message': (7, None),
         'security': (8, None),
         'message_type': (9, None),
         'message_control_id': (10, None),
         'processing_id': (11, None),
         'version_id': (12, None),
         'sequence_number': (13, None),
         'continuation_pointer': (14, None),
               }

bhs_transform = {\
         'batch_field_separator': (1, None),
         'batch_encoding_characters': (2, None),
         'batch_sending_application': (3, None),
         'batch_sending_facility': (4, None),
         'batch_rcving_application': (5, None),
         'batch_receiving_facility': (6, None),
         'batch_creation_datetime': (7, None),
         'batch_security': (8, None),
         'batch_nameidtype': (9, None),
         'batch_comment': (10, None),
         'batch_control_id': (11, None),
         'reference_batch_cntrl_id': (12, None),
               }

pv1_transform = {\
         'set_id': (1, None),
         'patient_class': (2, None),
         'assigned_patient_location': (3, None),
         'admission_type': (4, None),
         'preadmit_number': (5, None),
         'prior_patient_location': (6, None),
         'attending_doctor': (7, None),
         'refering_doctor': (8, None),
         'consulting_doctor': (9, None),
         'hospital_service': (10, None),
         'temporary_location': (11, None),
         'preadmit_test_indicator': (12, None),
         'readmission_indicator': (13, None),
         'admit_source': (14, None),
         'ambulatory_status': (15, None),
         'vip_indicators': (16, None),
         'admitting_doctor': (17, None),
         'patient_type': (18, None),
         'visit_number': (19, None),
         'financial_class': (20, None),
         'charge_price_indicator': (21, None),
         'courtesy_code': (22, None),
         'credit_rating': (23, None),
         'contract_code': (24, None),
         'contract_effective_date': (25, datetransform),
         'contract_amount': (26, None),
         'contract_period': (27, None),
         'interest_code': (28, None),
         'transfer_to_bad_debt_code': (29, None),
         'transfer_to_bad_debt_date': (30, datetransform),
         'bad_debt_agency_code': (31, None),
         'bad_debt_transfer_amount': (32, None),
         'bad_debt_recovery_amount': (33, None),
         'delete_account_indicator': (34, None),
         'delete_account_date': (35, datetransform),
         'discharge_disposition': (36, None),
         'discharged_to_location': (37, None),
         'diet_type': (38, None),
         'servicing_facility': (39, None),
         'bed_status': (40, None),
         'account_status': (41, None),
         'pending_location': (42, None),
         'prior_temporary_location': (43, None),
         'admit_datetime': (44, None),
         'discharge_datetime': (45, None),
         'current_patient_balance': (46, None),
         'total_charges': (47, None),
         'total_adjustments': (48, None),
         'total_payments': (49, None),
               }

npu_transform = {\
         'bed_location': (1, None),
         'bed_status': (2, None),
               }

bts_transform = {\
         'batch_message_count': (1, None),
         'batch_comment': (2, None),
         'batch_totals': (3, None),
               }

obr_transform = {\
         'set_id': (1, None),
         'placer_orders_': (2, None),
         'fillers_order_': (3, None),
         'universal_service_id': (4, None),
         'priority': (5, None),
         'requested_datetime': (6, None),
         'observation_datetime': (7, None),
         'observation_end_datetime': (8, None),
         'collection_volume': (9, None),
         'collector_identifier': (10, None),
         'specimen_action_code': (11, None),
         'danger_code': (12, None),
         'relevant_clinical_info': (13, None),
         'specimen_rcvd_datetime': (14, None),
         'specimen_source': (15, None),
         'ordering_provider': (16, None),
         'order_call_back_phone_num': (17, None),
         'placers_field_1': (18, None),
         'placers_field_2': (19, None),
         'fillers_field_1': (20, None),
         'fillers_field_2': (21, None),
         'results_rptstatus_chgdt': (22, None),
         'charge_to_practice': (23, None),
         'diagnostic_serv_sect_id': (24, None),
         'result_status': (25, None),
         'linked_results': (26, None),
         'quantitytiming': (27, None),
         'result_copies_to': (28, None),
         'parent_accession_': (29, None),
         'transportation_mode': (30, None),
         'reason_for_study': (31, None),
         'prin_result_interpreter': (32, None),
         'asst_result_interpreter': (33, None),
         'technician': (34, None),
         'transcriptionist': (35, None),
         'scheduled_datetime': (36, None),
               }

pr1_transform = {\
         'set_id': (1, None),
         'procedure_coding_method': (2, None),
         'procedure_code': (3, None),
         'procedure_description': (4, None),
         'procedure_datetime': (5, None),
         'procedure_type': (6, None),
         'procedure_minutes': (7, None),
         'anesthesiologist': (8, None),
         'anesthesia_code': (9, None),
         'anesthesia_minutes': (10, None),
         'surgeon': (11, None),
         'resident_code': (12, None),
         'consent_code': (13, None),
               }

fts_transform = {\
         'file_batch_count': (1, None),
         'file_trailer_comment': (2, None),
               }

urd_transform = {\
         'ru_datetime': (1, None),
         'report_priority': (2, None),
         'ru_who_subject_defnition': (3, None),
         'ru_what_subject_defntion': (4, None),
         'ru_what_department_code': (5, None),
         'ru_displayprint_locs': (6, None),
         'ru_results_level': (7, datetransform),
               }

urs_transform = {\
         'ru_where_subject_def': (1, None),
         'ru_when_start_dtetme': (2, None),
         'ru_when_end_dtetme': (3, None),
         'ru_what_user_qualifier': (4, None),
         'ru_oth_results_def': (5, None),
               }

blg_transform = {\
         'when_to_charge': (1, None),
         'value_type': (2, None),
         'observation_identifier': (3, None),
               }

oro_transform = {\
         'order_item_id': (1, None),
         'substitute_allowed': (2, None),
         'results_copied_to': (3, None),
         'stock_location': (4, None),
               }

orc_transform = {\
         'order_control': (1, None),
         'placer_order_': (2, None),
         'filler_order_': (3, None),
         'placer_order_': (4, None),
         'order_status': (5, None),
         'response_flag': (6, None),
         'timingquantity': (7, None),
         'parent': (8, None),
         'datetime_of_transaction': (9, None),
         'entered_by': (10, None),
         'verified_by': (11, None),
         'ordering_provider': (12, None),
         'enterers_location': (13, None),
         'call_back_phone_number': (14, None),
               }

ft1_transform = {\
         'set_id': (1, None),
         'transaction_id': (2, None),
         'transaction_batch_id': (3, None),
         'transaction_date': (4, datetransform),
         'transaction_posting_date': (5, datetransform),
         'transaction_type': (6, None),
         'transaction_code': (7, None),
         'transaction_description': (8, None),
         'transaction_description__alternative': (9, None),
         'transaction_quantity': (10, None),
         'transaction_amount__ext': (11, None),
         'transaction_amount__unit': (12, None),
         'department_code': (13, None),
         'insurance_plan_id': (14, None),
         'insurance_amount': (15, None),
         'patient_location': (16, None),
         'fee_schedule': (17, None),
         'patient_type': (18, None),
         'diagnosis_code': (19, None),
         'performed_by_code': (20, None),
         'ordered_by_code': (21, None),
         'unit_cost': (22, None),
               }

nk1_transform = {\
         'set_id': (1, None),
         'next_of_kin_name': (2, None),
         'next_of_kin_relationship': (3, None),
         'next_of_kin_address': (4, None),
         'next_of_kin_phone_number': (5, None),
               }

dg1_transform = {\
         'set_id': (1, None),
         'diagnosis_coding_method': (2, None),
         'diagnosis_code': (3, None),
         'diagnosis_description': (4, None),
         'diagnosis_datetime': (5, None),
         'diagnosisdrg_type': (6, None),
         'major_diagnostic_category': (7, None),
         'diagnostic_related_group': (8, None),
         'drg_approval_indicator': (9, None),
         'drg_grouper_review_code': (10, None),
         'outlier_type': (11, None),
         'outlier_days': (12, None),
         'outlier_cost': (13, None),
         'grouper_version_and_type': (14, None),
               }

err_transform = {\
         'error_code_and_location': (1, None),
               }

qrd_transform = {\
         'query_datetime': (1, None),
         'query_format_code': (2, None),
         'query_priority': (3, None),
         'query_id': (4, None),
         'deferred_response_type': (5, None),
         'def_resp_datetime': (6, None),
         'quantity_limited_request': (7, None),
         'who_subject_filter': (8, None),
         'what_subject_filter': (9, None),
         'what_dept_data_code': (10, None),
         'what_data_cd_value_qua': (11, None),
         'query_results_level': (12, None),
               }

add_transform = {\
         '1': (1, None),
               }

in1_transform = {\
         'set_id': (1, None),
         'insurance_plan_id': (2, None),
         'insurance_company_id': (3, None),
         'insurance_company_name': (4, None),
         'insurance_company_address': (5, None),
         'insurance_co_contact_pers': (6, None),
         'insurance_co_phone_number': (7, None),
         'group_number': (8, None),
         'group_name': (9, None),
         'insureds_group_emp_id': (10, None),
         'insureds_group_emp_name': (11, None),
         'plan_effective_date': (12, datetransform),
         'plan_expiration_date': (13, datetransform),
         'authorization_information': (14, None),
         'plan_type': (15, None),
         'name_of_insured': (16, None),
         'insureds_relation_to_pat': (17, None),
         'insureds_date_of_birth': (18, datetransform),
         'insureds_address': (19, None),
         'assignment_of_benefits': (20, None),
         'coordination_of_benefits': (21, None),
         'coord_of_ben_priority': (22, None),
         'notice_of_admission_code': (23, None),
         'notice_of_admission_date': (24, datetransform),
         'rpt_of_eligibility_code': (25, None),
         'rpt_of_eligibility_date': (26, datetransform),
         'release_information_code': (27, None),
         'preadmit_cert_pac': (28, None),
         'verification_date': (29, datetransform),
         'verification_by': (30, None),
         'type_of_agreement_code': (31, None),
         'billing_status': (32, None),
         'lifetime_reserve_days': (33, None),
         'delay_before_l_r_day': (34, None),
         'company_plan_code': (35, None),
         'policy_number': (36, None),
         'policy_deductible': (37, None),
         'policy_limit__amount': (38, None),
         'policy_limit__days': (39, None),
         'room_rate__semiprivate': (40, None),
         'room_rate__private': (41, None),
         'insureds_employ_status': (42, None),
         'insureds_sex': (43, None),
         'insureds_employer_addresss': (44, None),
               }

msa_transform = {\
         'acknowledgement_code': (1, None),
         'message_control_id': (2, None),
         'text_message': (3, None),
         'expected_sequence_number': (4, None),
         'delayed_ack_type': (5, None),
               }

