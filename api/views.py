from django.shortcuts import render
from django.http import HttpResponse
from .utils import ordinal_number

def likelion_shield_badge(request):
  generation = request.GET.get('generation') or 9

  svg = '''
  <svg height="20" width="110" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 103.37 20">
    <defs>
      <style>
        <![CDATA[
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800&display=swap');
        ]]>
        .cls-1,.cls-3{{
          fill: #231815;
        }}
        .cls-2{{
          fill: #f39800;
        }}
        .cls-3{{
          isolation:isolate;
          font-size:13px;
          font-family:Montserrat-ExtraBold, Montserrat;font-weight:800;
        }}
        .cls-4{{
          fill:#f29f00;
        }}
      </style>
    </defs>
    <g id="레이어_2" data-name="레이어 2">
      <g id="레이어_1-2" data-name="레이어 1">
        <g id="레이어_2-2" data-name="레이어 2">
          <g id="레이어_1-2-2" data-name="레이어 1-2">
            <g id="레이어_1-2-2-2" data-name="레이어 1-2-2">
              <path class="cls-1" d="M3.63,0H99.74a3.59,3.59,0,0,1,3.63,3.55h0V16.44A3.59,3.59,0,0,1,99.75,20H3.63A3.6,3.6,0,0,1,0,16.44V3.56A3.6,3.6,0,0,1,3.63,0Z"/>
              <path class="cls-2" d="M67.3,0H99.74a3.59,3.59,0,0,1,3.63,3.55h0V16.44A3.59,3.59,0,0,1,99.75,20H67.3"/>
              <text class="cls-3" text-anchor="middle" transform="translate(84.79 14.35)">
                {generation_ordinal_number}
              </text>
            </g>
          </g>
        </g>
        <polygon class="cls-4" points="4.2 5.63 6.11 5.63 6.11 12.62 10.61 12.62 10.61 14.35 4.2 14.35 4.2 5.63"/>
        <rect class="cls-4" x="11.72" y="5.63" width="1.92" height="8.72"/>
        <polygon class="cls-4" points="15.05 5.63 16.97 5.63 16.97 9.37 20.51 5.63 22.82 5.63 19.27 9.33 22.99 14.35 20.68 14.35 17.98 10.63 16.97 11.68 16.97 14.35 15.05 14.35 15.05 5.63"/>
        <polygon class="cls-4" points="23.7 5.63 30.49 5.63 30.49 7.33 25.59 7.33 25.59 9.13 30.27 9.13 30.27 10.84 25.59 10.84 25.59 12.64 30.49 12.64 30.49 14.35 23.7 14.35 23.7 5.63"/>
        <polygon class="cls-4" points="33.91 5.63 35.83 5.63 35.83 12.62 40.32 12.62 40.32 14.35 33.91 14.35 33.91 5.63"/><rect class="cls-4" x="41.42" y="5.63" width="1.92" height="8.72"/>
        <polygon class="cls-4" points="54.76 5.63 56.6 5.63 60.69 11 60.69 5.63 62.67 5.63 62.67 14.35 60.95 14.35 56.73 8.8 56.73 14.35 54.76 14.35 54.76 5.63"/>
        <path class="cls-4" d="M49,14.59a4.82,4.82,0,0,1-1.89-.36,4.76,4.76,0,0,1-1.49-1,4.49,4.49,0,0,1-1-1.44A4.62,4.62,0,0,1,44.3,10v0a4.42,4.42,0,0,1,.35-1.78,4.69,4.69,0,0,1,1-1.46,4.56,4.56,0,0,1,1.5-1A4.89,4.89,0,0,1,49,5.41a4.82,4.82,0,0,1,1.89.36,4.65,4.65,0,0,1,1.49,1,4.33,4.33,0,0,1,1,1.44A4.63,4.63,0,0,1,53.73,10v0a4.59,4.59,0,0,1-1.34,3.24,4.56,4.56,0,0,1-1.5,1,4.86,4.86,0,0,1-1.89.36m0-1.76a2.67,2.67,0,0,0,1.1-.22A2.61,2.61,0,0,0,51,12a2.76,2.76,0,0,0,.55-.9,2.8,2.8,0,0,0,.2-1.08v0a2.82,2.82,0,0,0-.2-1.09A2.59,2.59,0,0,0,51,8a2.68,2.68,0,0,0-.87-.61,2.78,2.78,0,0,0-2.19,0,2.73,2.73,0,0,0-.85.6,2.76,2.76,0,0,0-.55.9A3,3,0,0,0,46.3,10v0a3,3,0,0,0,.2,1.09,2.59,2.59,0,0,0,.56.9,2.87,2.87,0,0,0,.86.61,2.64,2.64,0,0,0,1.1.23"/>
      </g>
    </g>
  </svg>'''.format(
      generation_ordinal_number=ordinal_number(generation),
    )

  response = HttpResponse(content=svg)
  response['Content-Type'] = 'image/svg+xml'
  response['Cache-Control'] = 'no-cache'
  return response

def likelion_university_badge_v1(request):
  generation = request.GET.get('generation') or 9
  university = request.GET.get('university')

  svg= '''
    <svg height="200" width="723.646" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 479.85 132.62">
      <defs>
        <style>
          <![CDATA[
          @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800&display=swap');
          ]]>
          .cls-1,.cls-2{{
            fill:#120b0c;
          }}
          .cls-2,.cls-3{{
            stroke:#f19700;
          }}
          .cls-2,.cls-3,.cls-5{{
            stroke-miterlimit:10;
          }}
          .cls-2{{
            stroke-width:0.5px;
          }}
          .cls-3,.cls-4,.cls-7,.cls-8{{
            fill:#f2a000;
          }}
          .cls-5{{
            font-size:13.92px;
            fill:#231815;
            stroke:#f2a000;
            stroke-width:0.4px;
            letter-spacing:-0.02em;
          }}
          .cls-5,.cls-7,.cls-8{{
            font-family:Montserrat-ExtraBold, Montserrat;font-weight:800;
          }}
          .cls-6{{
            letter-spacing:0em;
          }}
          .cls-7{{
            font-size:21.14px;
          }}
          .cls-8{{
            font-size:16.59px;
          }}
        </style>
      </defs>
      <g id="레이어_2" data-name="레이어 2">
        <g id="레이어_1-2" data-name="레이어 1">
        <rect class="cls-1" width="479.85" height="132.62" rx="11.76"/>
        <polygon class="cls-2" points="105.89 55.64 105.89 28.02 147.78 28.02 105.89 55.64"/>
        <polygon class="cls-3" points="62.79 80.53 62.79 28.01 18.39 28.01 59.86 55.36 59.86 92.99 105.89 92.99 105.89 89.45 105.89 88.09 105.89 80.53 62.79 80.53"/>
        <polygon class="cls-4" points="183.44 39.54 191.66 39.54 191.66 69.47 210.9 69.47 210.9 76.89 183.44 76.89 183.44 39.54"/>
        <rect class="cls-4" x="215.66" y="39.54" width="8.22" height="37.35"/>
        <polygon class="cls-4" points="229.95 39.54 238.17 39.54 238.17 55.57 253.32 39.54 263.24 39.54 248.04 55.39 263.94 76.89 254.07 76.89 242.49 60.99 238.17 65.47 238.17 76.89 229.95 76.89 229.95 39.54"/>
        <polygon class="cls-4" points="267 39.54 296.06 39.54 296.06 46.85 275.1 46.85 275.1 54.56 295.11 54.56 295.11 61.87 275.1 61.87 275.1 69.58 296.06 69.58 296.06 76.89 267 76.89 267 39.54"/>
        <polygon class="cls-4" points="310.71 39.54 318.93 39.54 318.93 69.47 338.17 69.47 338.17 76.89 310.71 76.89 310.71 39.54"/>
        <rect class="cls-4" x="342.88" y="39.54" width="8.22" height="37.35"/>
        <polygon class="cls-4" points="400.01 39.54 407.92 39.54 425.42 62.54 425.42 39.54 433.89 39.54 433.89 76.89 426.54 76.89 408.45 53.15 408.45 76.89 400.01 76.89 400.01 39.54"/>
        <path class="cls-4" d="M375.35,77.93a20.72,20.72,0,0,1-8.09-1.55,20.18,20.18,0,0,1-6.38-4.18A18.55,18.55,0,0,1,356.7,66a19.45,19.45,0,0,1-1.5-7.63v-.11a19.25,19.25,0,0,1,1.52-7.63,20,20,0,0,1,4.21-6.25,19.57,19.57,0,0,1,6.41-4.23,22,22,0,0,1,16.21,0,20,20,0,0,1,6.38,4.18,18.86,18.86,0,0,1,4.18,6.19,19.62,19.62,0,0,1,1.49,7.63v.11a19.48,19.48,0,0,1-12.13,18.11,21,21,0,0,1-8.12,1.55m.11-7.55a11.64,11.64,0,0,0,4.68-.93,10.82,10.82,0,0,0,3.66-2.59A12.21,12.21,0,0,0,386.17,63a12.59,12.59,0,0,0,.85-4.65v-.11a12.83,12.83,0,0,0-.85-4.68A11.57,11.57,0,0,0,380,47.12a11.4,11.4,0,0,0-4.68-1,11.58,11.58,0,0,0-4.71.94A10.7,10.7,0,0,0,367,49.68a12.26,12.26,0,0,0-2.36,3.82,12.69,12.69,0,0,0-.86,4.66v.11a12.83,12.83,0,0,0,.86,4.68,11.64,11.64,0,0,0,6.11,6.47,11.27,11.27,0,0,0,4.71,1"/>
        <path class="cls-4" d="M191.81,92.29h-7.73V84.76h7.73v2.72h2.95V83.6h2.35v11h-2.35v-5.2h-2.95Zm1,1.78a2.87,2.87,0,0,0,.31,1.28,3.66,3.66,0,0,0,1,1.19,5.78,5.78,0,0,0,1.61,1,8.7,8.7,0,0,0,2.28.6l-.85,1.83a9.15,9.15,0,0,1-3.4-1.14,6.13,6.13,0,0,1-2.12-2,6.26,6.26,0,0,1-2.13,2,9,9,0,0,1-3.37,1.14l-.86-1.83a8.37,8.37,0,0,0,2.26-.61,7,7,0,0,0,1.62-1,4.11,4.11,0,0,0,1-1.19,2.79,2.79,0,0,0,.32-1.24v-.45h2.39Zm-3.31-7.46h-3.12v3.84h3.12Z"/>
        <path class="cls-4" d="M205.5,92.82a5,5,0,0,1-1.67-1.06,5.19,5.19,0,0,1-1.07-1.5A6.28,6.28,0,0,1,201.57,92a5.09,5.09,0,0,1-1.86,1.21l-1.21-1.81a5.14,5.14,0,0,0,1.41-.85,5,5,0,0,0,1-1.11,4.42,4.42,0,0,0,.54-1.29,5.71,5.71,0,0,0,.17-1.37v-.12H199V84.81h7.24v1.87h-2.42v.12a5.17,5.17,0,0,0,.16,1.31,4.14,4.14,0,0,0,.51,1.18,4.55,4.55,0,0,0,.88,1,4.28,4.28,0,0,0,1.3.73Zm1.64,1a11.72,11.72,0,0,1,2.32.22,6.3,6.3,0,0,1,1.78.61,3.23,3.23,0,0,1,1.13,1,2.4,2.4,0,0,1,0,2.62,3.23,3.23,0,0,1-1.13,1,6.3,6.3,0,0,1-1.78.61,12.45,12.45,0,0,1-4.66,0,6.37,6.37,0,0,1-1.79-.61,3.23,3.23,0,0,1-1.13-1,2.3,2.3,0,0,1,0-2.62,3.23,3.23,0,0,1,1.13-1A6.37,6.37,0,0,1,204.8,94a11.78,11.78,0,0,1,2.34-.22m0,4.44a7.31,7.31,0,0,0,2.43-.32c.56-.22.84-.55.84-1s-.28-.78-.84-1a7.31,7.31,0,0,0-2.43-.32,7.41,7.41,0,0,0-2.47.32c-.56.22-.85.55-.85,1s.29.78.85,1a7.41,7.41,0,0,0,2.47.32m2.1-5.18h-2.17V83.92h2.17v3.61h1.23V83.6h2.22v9.93h-2.22V89.44h-1.23Z"/>
        <path class="cls-4" d="M218.44,84.74a3.73,3.73,0,0,1,1.72.41,4,4,0,0,1,1.36,1.16,6,6,0,0,1,.9,1.84,8.3,8.3,0,0,1,.33,2.43,8.42,8.42,0,0,1-.33,2.44,6,6,0,0,1-.9,1.85,4,4,0,0,1-1.36,1.18,3.72,3.72,0,0,1-1.72.4,3.68,3.68,0,0,1-1.71-.4,4.05,4.05,0,0,1-1.37-1.18,6,6,0,0,1-.9-1.85,8.42,8.42,0,0,1-.33-2.44,8.3,8.3,0,0,1,.33-2.43,6,6,0,0,1,.9-1.84,4,4,0,0,1,1.37-1.16,3.69,3.69,0,0,1,1.71-.41m0,2.12a1.68,1.68,0,0,0-1.47.94,5.47,5.47,0,0,0-.57,2.78,5.54,5.54,0,0,0,.57,2.79,1.62,1.62,0,0,0,2.95,0,5.54,5.54,0,0,0,.57-2.79,5.47,5.47,0,0,0-.57-2.78,1.68,1.68,0,0,0-1.48-.94M227.26,100h-2.35V83.58h2.35Z"/>
        <path class="cls-4" d="M238.37,87.25a10.71,10.71,0,0,0,.22,2.19,8.84,8.84,0,0,0,.69,2,6.85,6.85,0,0,0,1.17,1.73,5.67,5.67,0,0,0,1.71,1.26l-1.42,1.85a6.28,6.28,0,0,1-2.16-1.8,9.5,9.5,0,0,1-1.4-2.62,9.89,9.89,0,0,1-1.47,2.81,6.44,6.44,0,0,1-2.33,1.91l-1.4-1.9a6,6,0,0,0,1.79-1.28,7.69,7.69,0,0,0,1.24-1.8,9.08,9.08,0,0,0,.73-2.13,10.87,10.87,0,0,0,.24-2.27V84.86h2.39Zm9.17,4.61h-2.39V100H242.8V83.6h2.35v6.3h2.39Z"/>
        <path class="cls-4" d="M254.36,88a8,8,0,0,0,1,3.8,7.41,7.41,0,0,0,1.23,1.64,6.17,6.17,0,0,0,1.77,1.21l-1.3,1.85a6.4,6.4,0,0,1-2.33-1.79,9.46,9.46,0,0,1-1.5-2.63A10.1,10.1,0,0,1,251.69,95a6.6,6.6,0,0,1-2.39,1.94L248,95.05a5.71,5.71,0,0,0,1.77-1.24A7.63,7.63,0,0,0,251,92.08a8.34,8.34,0,0,0,.76-2A9.29,9.29,0,0,0,252,88v-.9h-3.4V85.17h9v1.94h-3.26Zm9.2,3.78h-2.38V100h-2.35V83.6h2.35v6.25h2.38Z"/>
        <path class="cls-4" d="M270.49,88.71a7,7,0,0,0,2.17,5.06,6.34,6.34,0,0,0,1.73,1.14l-1.25,1.79a6.48,6.48,0,0,1-2.3-1.7,8.2,8.2,0,0,1-1.49-2.48,8.5,8.5,0,0,1-1.48,2.65,6.2,6.2,0,0,1-2.35,1.8l-1.24-1.8A6.28,6.28,0,0,0,266,94a7.12,7.12,0,0,0,1.21-1.59,7.41,7.41,0,0,0,.71-1.81,8.19,8.19,0,0,0,.23-1.88v-.57h-3.31V86.27h3.31V84h2.35v2.28h3.26v1.87h-3.26Zm7.64-5.11V100h-2.35V91.77h-2.9v-1.9h2.9V83.6Z"/>
        <path class="cls-4" d="M289.35,92.41c-.57.1-1.14.17-1.69.22l-1.72.11c-.59,0-1.21.05-1.85.06h-3.43V87.66h5V86.25h-5.07V84.38H288v5h-5v1.53l1.71,0c.53,0,1.05,0,1.55-.06s1-.07,1.47-.12,1-.11,1.47-.19Zm-6.59,1.53h11V99.8h-11Zm2.31,4h6.36V95.78h-6.36Zm8.68-14.37v9.65H291.4v-4.4h-2.55V87h2.55V83.6Z"/>
        <text class="cls-5" text-anchor="end" transform="translate(434.62 36.12)">
          {generation_ordinal_number}
        </text>
        <text class="cls-8" transform="translate(298.78 99.8)">
          {university_seperator}
        </text>
        <text class="cls-7" transform="translate(316.76 99.93)">
          {university}
        </text>
        </g>
      </g>
    </svg>
  '''.format(
    generation_ordinal_number=ordinal_number(generation),
    university = university or "",
    university_seperator = 'X' if university else '' 
  )
  response = HttpResponse(content=svg)
  response['Content-Type'] = 'image/svg+xml'
  response['Cache-Control'] = 'no-cache'
  return response
