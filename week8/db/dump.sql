--
-- PostgreSQL database dump
--

-- Dumped from database version 12.9 (Ubuntu 12.9-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.9 (Ubuntu 12.9-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: cities; Type: TABLE; Schema: public; Owner: kalashovich
--

CREATE TABLE public.cities (
    name character varying(80),
    country character varying(80),
    location point,
    id integer NOT NULL
);


ALTER TABLE public.cities OWNER TO kalashovich;

--
-- Name: cities_id_seq; Type: SEQUENCE; Schema: public; Owner: kalashovich
--

CREATE SEQUENCE public.cities_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cities_id_seq OWNER TO kalashovich;

--
-- Name: cities_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kalashovich
--

ALTER SEQUENCE public.cities_id_seq OWNED BY public.cities.id;


--
-- Name: weathers; Type: TABLE; Schema: public; Owner: kalashovich
--

CREATE TABLE public.weathers (
    city character varying(80),
    temp_low integer,
    temp_high integer,
    prcp real,
    data date,
    id integer NOT NULL
);


ALTER TABLE public.weathers OWNER TO kalashovich;

--
-- Name: weathers_id_seq; Type: SEQUENCE; Schema: public; Owner: kalashovich
--

CREATE SEQUENCE public.weathers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.weathers_id_seq OWNER TO kalashovich;

--
-- Name: weathers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kalashovich
--

ALTER SEQUENCE public.weathers_id_seq OWNED BY public.weathers.id;


--
-- Name: cities id; Type: DEFAULT; Schema: public; Owner: kalashovich
--

ALTER TABLE ONLY public.cities ALTER COLUMN id SET DEFAULT nextval('public.cities_id_seq'::regclass);


--
-- Name: weathers id; Type: DEFAULT; Schema: public; Owner: kalashovich
--

ALTER TABLE ONLY public.weathers ALTER COLUMN id SET DEFAULT nextval('public.weathers_id_seq'::regclass);


--
-- Data for Name: cities; Type: TABLE DATA; Schema: public; Owner: kalashovich
--

COPY public.cities (name, country, location, id) FROM stdin;
BIshkek	Kyrgyzstan	(-184,84)	1
Osh	Kyrgyzstan	(-175,19)	2
\.


--
-- Data for Name: weathers; Type: TABLE DATA; Schema: public; Owner: kalashovich
--

COPY public.weathers (city, temp_low, temp_high, prcp, data, id) FROM stdin;
Bishkek	-14	-3	0.1	2021-01-20	1
Bishkek	-18	-9	0	2022-07-15	2
OSH	21	45	0	2021-09-20	3
San-Francisco	27	52	0.25	1994-11-30	4
San-Francisco	13	34	1	1994-10-21	5
\.


--
-- Name: cities_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kalashovich
--

SELECT pg_catalog.setval('public.cities_id_seq', 2, true);


--
-- Name: weathers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kalashovich
--

SELECT pg_catalog.setval('public.weathers_id_seq', 5, true);


--
-- Name: cities cities_name_key; Type: CONSTRAINT; Schema: public; Owner: kalashovich
--

ALTER TABLE ONLY public.cities
    ADD CONSTRAINT cities_name_key UNIQUE (name);


--
-- Name: cities cities_pkey; Type: CONSTRAINT; Schema: public; Owner: kalashovich
--

ALTER TABLE ONLY public.cities
    ADD CONSTRAINT cities_pkey PRIMARY KEY (id);


--
-- Name: weathers weathers_pkey; Type: CONSTRAINT; Schema: public; Owner: kalashovich
--

ALTER TABLE ONLY public.weathers
    ADD CONSTRAINT weathers_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

